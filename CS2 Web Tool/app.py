import os
import re
from flask import Flask, render_template, request, jsonify, session
from functools import wraps
import logging

logging.getLogger('waitress').setLevel(logging.WARNING)  # Suppress Flask's default request logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'change-this-secret-key')

# ── Config (set via environment variables) ──────────────────────────────────
RCON_HOST      = os.environ.get('RCON_HOST', '192.168.1.41')
RCON_PORT      = int(os.environ.get('RCON_PORT', 27015))
RCON_PASSWORD  = os.environ.get('RCON_PASSWORD', '')
CONTAINER_NAME = os.environ.get('CS2_CONTAINER', 'cs2')
WEB_PORT       = int(os.environ.get('WEB_PORT', 5000))

# ── Users ────────────────────────────────────────────────────────────────────
USERS = {
    'Jacob':   os.environ.get('PASS_JACOB',   'Gh0s7!'),
    'Chris':   os.environ.get('PASS_CHRIS',   'Chris'),
    'Jonno':   os.environ.get('PASS_JONNO',   'Jonno13'),
    'Nuclear': os.environ.get('PASS_NUCLEAR', 'option'),
}

# ── Official maps ─────────────────────────────────────────────────────────────
MAPS = {
    'Ancient':      'de_ancient',
    'Ancient Night':'de_ancient_night',
    'Anubis':       'de_anubis',
    'Dust 2':       'de_dust2',
    'Inferno':      'de_inferno',
    'Italy':        'cs_italy',
    'Mirage':       'de_mirage',
    'Nuke':         'de_nuke',
    'Office':       'cs_office',
    'Overpass':     'de_overpass',
    'Train':        'de_train',
    'Vertigo':      'de_vertigo',
    'Baggage':      'ar_baggage',
    'Shoots':       'ar_shoots',
    'Shoots Night': 'ar_shoots_night',
}

# ── Workshop maps  (gamemode_alias, workshop_id) ──────────────────────────────
WORKSHOP_MAPS = {
    'Bomb': {
        'Foroglio':    ('casual', 3132854332),
        'Assembly':    ('casual', 3071005299),
        'Black Gold':  ('casual', 3075012302),
        'Lake':        ('casual', 3070563536),
        'Bank':        ('casual', 3070581293),
        'Bikini Bottom':('casual',3204870970),
        'Plane':       ('casual', 3217247541),
        'St Marc':     ('casual', 3070562370),
        'Sugarcane':   ('casual', 3070579459),
        'Astra':       ('casual', 3083296922),
        'Maginot':     ('casual', 3195399109),
        'Palais':      ('casual', 3257582863),
        'Omaha Beach': ('casual', 3148007939),
        'Train':       ('casual', 3070284539),
        'Attic':       ('casual', 3305148449),
        'The Metro':   ('casual', 3326236589),
        'Cache':       ('casual', 3328271311),
        'Inca':        ('casual', 3325387224),
        'Sparity':     ('casual', 3317923634),
        'Basalt':      ('casual', 3329258290),
        'Zoo':         ('casual', 3101352333),
        'Tuscan':      ('casual', 3267671493),
        'Rainfall':    ('casual', 3265650949),
        'Lighthouse':  ('casual', 3342529755),
        'Refuse':      ('casual', 3294609675),
    },
    'Hostage': {
        'Rush':        ('casual', 3077752384),
        'Safehouse':   ('casual', 3070550406),
        'Minecraft':   ('casual', 3095875614),
        'Dam':         ('casual', 3072481684),
        'Assault':     ('casual', 3079872050),
        'Rainbow 6':   ('casual', 3115452448),
        'Militia':     ('casual', 3202169771),
        'HiJack':      ('casual', 3310206718),
        'Climb':       ('casual', 3319649237),
        'Agency':      ('casual', 3339983232),
        'Paris 2024':  ('casual', 3344069159),
    },
    'Arms Race': {
        'Lunacy':      ('armsrace', 3070560242),
        'Monastery':   ('armsrace', 3070547153),
        'St Marc':     ('armsrace', 3070562370),
        'Stairs':      ('armsrace', 3264733671),
        'Churches':    ('armsrace', 3070291913),
        'Pool Day':    ('armsrace', 3070923343),
        'Speedball':   ('armsrace', 3111527644),
    },
    'Deathmatch': {
        'Omaha Beach': ('deathmatch', 3148007939),
        'Astra':       ('deathmatch', 3083296922),
        'Halo':        ('deathmatch', 3255907412),
        'Breadwindow': ('deathmatch', 3371417956),
        'Eternal':     ('deathmatch', 3094002407),
        'Mansion':     ('deathmatch', 3080114822),
        'AI Reality':  ('deathmatch', 3105649124),
        'Lighthouse':  ('deathmatch', 3342529755),
        'Dolls House': ('deathmatch', 3073384529),
        'Lake':        ('deathmatch', 3070563536),
    },
}

GAMEMODE_CMDS = {
    'casual':     'game_alias casual',
    'armsrace':   'game_type 1; game_mode 0; sv_skirmish_id 10',
    'deathmatch': 'game_alias deathmatch',
}

# ── RCON helper ───────────────────────────────────────────────────────────────
def rcon_command(command):
    try:
        from rcon.source import Client
        with Client(RCON_HOST, RCON_PORT, passwd=RCON_PASSWORD) as client:
            return {'ok': True, 'result': client.run(command)}
    except Exception as e:
        return {'ok': False, 'error': str(e)}

def parse_status(status_output):
    players = []
    current_map = 'Unknown'
    in_players = False

    for line in status_output.split('\n'):
        # Map — grab from first spawngroup entry
        if current_map == 'Unknown' and '[1:' in line and '| main lump' in line:
            m = re.search(r'\[1:\s*(\S+)\s*\|', line)
            if m:
                current_map = m.group(1)

        # Detect start of players table
        if line.strip().startswith('id') and 'ping' in line and 'name' in line:
            in_players = True
            continue

        if not in_players:
            continue

        # Skip connecting/challenging slots (id 65535)
        if re.match(r'^\s*65535\b', line):
            continue

        # Real player: has an IP address in the line
        m = re.match(
            r'^\s*(\d+)\s+(\d+:\d+)\s+(\d+)\s+(\d+)\s+(\w+)\s+(\d+)\s+(\d+\.\d+\.\d+\.\d+:\d+)\s+\'(.*?)\'',
            line
        )
        if m:
            userid, time_, ping, loss, state, rate, addr, name = m.groups()
            if state == 'active' and name:
                players.append({'userid': userid, 'name': name, 'ping': ping, 'addr': addr})
            continue

        # Bot: has BOT where time would be
        m = re.match(
            r'^\s*(\d+)\s+BOT\s+\d+\s+\d+\s+\w+\s+\d+\s+\'(.*?)\'',
            line
        )
        if m:
            userid, name = m.groups()
            if name:
                players.append({'userid': userid, 'name': name, 'ping': '-', 'addr': 'BOT'})

    return players, current_map

# ── Auth decorator ────────────────────────────────────────────────────────────
def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user' not in session:
            return jsonify({'error': 'Not logged in'}), 401
        return f(*args, **kwargs)
    return decorated

# ── Routes ────────────────────────────────────────────────────────────────────
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json or {}
    username = data.get('username', '').strip()
    password = data.get('password', '')
    if username in USERS and USERS[username] == password:
        session['user'] = username
        return jsonify({'success': True, 'username': username})
    return jsonify({'success': False, 'error': 'Invalid username or password'}), 401

@app.route('/api/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({'success': True})

@app.route('/api/status')
@login_required
def server_status():
    try:
        import docker
        dc = docker.from_env()
        container = dc.containers.get(CONTAINER_NAME)
        running = container.status == 'running'
    except Exception as e:
        return jsonify({'running': False, 'players': [], 'map': 'Unknown',
                        'error': str(e), 'user': session.get('user')})

    players = []
    current_map = 'Unknown'
    if running:
        r = rcon_command('status')
        if r['ok']:
            players, current_map = parse_status(r['result'])

    return jsonify({
        'running': running,
        'players': players,
        'map': current_map,
        'user': session.get('user'),
    })

@app.route('/api/maps')
@login_required
def get_maps():
    return jsonify({'maps': list(MAPS.keys()),
                    'workshop': {k: list(v.keys()) for k, v in WORKSHOP_MAPS.items()}})

@app.route('/api/map', methods=['POST'])
@login_required
def change_map():
    data = request.json or {}
    name = data.get('map')
    if name not in MAPS:
        return jsonify({'error': 'Unknown map'}), 400
    rcon_command('game_alias casual')  # Ensure we're in a gamemode before changing map
    r = rcon_command(f'map {MAPS[name]}')
    return jsonify(r)

@app.route('/api/workshop', methods=['POST'])
@login_required
def workshop_map():
    data = request.json or {}
    category = data.get('category')
    name = data.get('map')
    if category not in WORKSHOP_MAPS or name not in WORKSHOP_MAPS[category]:
        return jsonify({'error': 'Unknown workshop map'}), 400

    gamemode, map_id = WORKSHOP_MAPS[category][name]
    if gamemode in GAMEMODE_CMDS:
        rcon_command(GAMEMODE_CMDS[gamemode])
    r = rcon_command(f'host_workshop_map {map_id}')
    return jsonify(r)

@app.route('/api/kick', methods=['POST'])
@login_required
def kick_player():
    data = request.json or {}
    userid = data.get('userid', '').strip()
    if not userid or not userid.isdigit():
        return jsonify({'error': 'Invalid userid'}), 400
    rcon_command('sv_kick_ban_duration 3')
    r = rcon_command(f'kickid {userid}')
    return jsonify(r)

@app.route('/api/rcon', methods=['POST'])
@login_required
def raw_rcon():
    data = request.json or {}
    command = data.get('command', '').strip()
    ALLOWED = {'bot_add_ct', 'bot_add_t', 'bot_kick', 'bot_zombie 1', 'bot_zombie 0'}
    if command not in ALLOWED:
        return jsonify({'ok': False, 'error': 'Command not permitted'}), 403
    return jsonify(rcon_command(command))

@app.route('/api/server/start', methods=['POST'])
@login_required
def start_server():
    try:
        import docker
        dc = docker.from_env()
        container = dc.containers.get(CONTAINER_NAME)
        container.start()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/server/stop', methods=['POST'])
@login_required
def stop_server():
    try:
        import docker
        dc = docker.from_env()
        container = dc.containers.get(CONTAINER_NAME)
        container.stop()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    # print env vars for debugging
    print("RCON_HOST:", RCON_HOST)
    print("RCON_PORT:", RCON_PORT)
    print("RCON_PASSWORD:", RCON_PASSWORD)
    print("CONTAINER_NAME:", CONTAINER_NAME)
    print("WEB_PORT:", WEB_PORT)
    app.run(host='0.0.0.0', port=WEB_PORT, debug=False)
