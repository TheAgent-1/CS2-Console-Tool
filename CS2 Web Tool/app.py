import os
import re
from flask import Flask, render_template, request, jsonify, session
from functools import wraps
import logging
import time

logging.getLogger('waitress').setLevel(logging.WARNING)  # Suppress Flask's default request logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'change-this-secret-key')

# ── Config (set via environment variables) ──────────────────────────────────
#TEMP LOAD FROM .env. COMMENT OUT FOR PRODUCTION, SHOULD BE SET IN ENVIRONMENT
#from dotenv import load_dotenv
#load_dotenv()

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
GAMEMODES = {
    'Casual':            'game_alias casual',
    'Competitive':       'game_alias competitive',
    'Wingman':           'game_alias scrimcomp2v2',
    'Weapons Expert':    'game_alias scrimcomp5v5',
    'Deathmatch':        'game_alias deathmatch',
    'Arms Race':         'game_type 1; game_mode 0; sv_skirmish_id 10',
    'Demolition':        'game_type 1; game_mode 1; sv_skirmish_id 11',
    'Flying Scoutsman':  'game_type 0; game_mode 0; sv_skirmish_id 3',
    'Retakes':           'game_type 0; game_mode 0; sv_skirmish_id 12',
    'Guardian':          'game_alias cooperative',
}

# (mapname, type)  type used for filtering
MAPS = {
    'Ancient':       ('de_ancient',       'de'),
    'Ancient Night': ('de_ancient_night', 'de'),
    'Anubis':        ('de_anubis',        'de'),
    'Dust 2':        ('de_dust2',         'de'),
    'Inferno':       ('de_inferno',       'de'),
    'Italy':         ('cs_italy',         'cs'),
    'Mirage':        ('de_mirage',        'de'),
    'Nuke':          ('de_nuke',          'de'),
    'Office':        ('cs_office',        'cs'),
    'Overpass':      ('de_overpass',      'de'),
    'Train':         ('de_train',         'de'),
    'Vertigo':       ('de_vertigo',       'de'),
    'Baggage':       ('ar_baggage',       'ar'),
    'Shoots':        ('ar_shoots',        'ar'),
    'Shoots Night':  ('ar_shoots_night',  'ar'),
}

MODE_MAPS = {
    'Casual':           {'Ancient','Ancient Night','Anubis','Dust 2','Inferno','Italy','Mirage','Nuke','Office','Overpass','Train','Vertigo'},
    'Competitive':      {'Ancient','Anubis','Dust 2','Inferno','Italy','Mirage','Nuke','Office','Overpass','Train','Vertigo'},
    'Wingman':          {'Inferno','Nuke','Overpass','Vertigo'},
    'Weapons Expert':   {'Ancient','Anubis','Dust 2','Inferno','Italy','Mirage','Nuke','Office','Overpass','Train','Vertigo'},
    'Deathmatch':       {'Ancient','Anubis','Dust 2','Inferno','Italy','Mirage','Nuke','Office','Overpass','Train','Vertigo'},
    'Arms Race':        {'Baggage','Shoots','Shoots Night'},
    'Demolition':       {'Baggage','Shoots','Shoots Night'},
    'Flying Scoutsman': {'Ancient','Anubis','Dust 2','Inferno','Mirage','Nuke','Overpass','Train','Vertigo'},
    'Retakes':          {'Ancient','Anubis','Dust 2','Inferno','Mirage','Nuke','Overpass','Train','Vertigo'},
    'Guardian':         {'Ancient','Anubis','Dust 2','Inferno','Mirage','Nuke','Overpass','Train','Vertigo'},
}

# ── Workshop maps  (gamemode_alias, workshop_id) ──────────────────────────────
WORKSHOP_MAPS = {
    'Bomb': {
        'Foroglio':    ('Casual', 3132854332),
        'Assembly':    ('Casual', 3071005299),
        'Black Gold':  ('Casual', 3075012302),
        'Lake':        ('Casual', 3070563536),
        'Bank':        ('Casual', 3070581293),
        'Bikini Bottom':('Casual',3204870970),
        'Plane':       ('Casual', 3217247541),
        'St Marc':     ('Casual', 3070562370),
        'Sugarcane':   ('Casual', 3070579459),
        'Astra':       ('Casual', 3083296922),
        'Maginot':     ('Casual', 3195399109),
        'Palais':      ('Casual', 3257582863),
        'Omaha Beach': ('Casual', 3148007939),
        'Train':       ('Casual', 3070284539),
        'Attic':       ('Casual', 3305148449),
        'The Metro':   ('Casual', 3326236589),
        'Cache':       ('Casual', 3328271311),
        'Inca':        ('Casual', 3325387224),
        'Sparity':     ('Casual', 3317923634),
        'Basalt':      ('Casual', 3329258290),
        'Zoo':         ('Casual', 3101352333),
        'Tuscan':      ('Casual', 3267671493),
        'Rainfall':    ('Casual', 3265650949),
        'Lighthouse':  ('Casual', 3342529755),
        'Refuse':      ('Casual', 3294609675),
        'Stronghold':  ('Casual', 3477094554),
        'Warden':      ('Casual', 3256988376),
    },
    'Hostage': {
        'Rush':        ('Casual', 3077752384),
        'Safehouse':   ('Casual', 3070550406),
        'Minecraft':   ('Casual', 3095875614),
        'Dam':         ('Casual', 3072481684),
        'Assault':     ('Casual', 3079872050),
        'Rainbow 6':   ('Casual', 3115452448),
        'Militia':     ('Casual', 3202169771),
        'HiJack':      ('Casual', 3310206718),
        'Climb':       ('Casual', 3319649237),
        'Agency':      ('Casual', 3339983232),
        'Paris 2024':  ('Casual', 3344069159),
        'Alpine':      ('Casual', 3221291619),
    },
    'Arms Race': {
        'Lunacy':      ('Arms Race', 3070560242),
        'Monastery':   ('Arms Race', 3070547153),
        'St Marc':     ('Arms Race', 3070562370),
        'Stairs':      ('Arms Race', 3264733671),
        'Churches':    ('Arms Race', 3070291913),
        'Pool Day':    ('Arms Race', 3070923343),
        'Speedball':   ('Arms Race', 3111527644),
        
    },
    'Deathmatch': {
        'Omaha Beach': ('Deathmatch', 3148007939),
        'Astra':       ('Deathmatch', 3083296922),
        'Halo':        ('Deathmatch', 3255907412),
        'Breadwindow': ('Deathmatch', 3371417956),
        'Eternal':     ('Deathmatch', 3094002407),
        'Mansion':     ('Deathmatch', 3080114822),
        'AI Reality':  ('Deathmatch', 3105649124),
        'Lighthouse':  ('Deathmatch', 3342529755),
        'Dolls House': ('Deathmatch', 3073384529),
        'Lake':        ('Deathmatch', 3070563536),
        'Poseidon':    ('Deathmatch', 3522144043),
        'Warden':      ('Deathmatch', 3256988376),
    },
    'Wingman': {
        'Sanctum':     ('Wingman', 3643331442),
        'Poseidon':    ('Wingman', 3522144043),
    },
    'VIP': {
        'Ancient Night': ('Casual', 3575485852),
        'Ancient':       ('Casual', 3711700605),
        'Dust 2':        ('Casual', 3711705283),
        'Inferno':       ('Casual', 3711703660),
        'Anubis':        ('Casual', 3711702027),
        'Overpass':      ('Casual', 3711701554),
        'Vertigo':       ('Casual', 3711702590),
    },
}

# ── RCON helper ───────────────────────────────────────────────────────────────
def rcon_command(command):
    try:
        from rcon.source import Client
        with Client(RCON_HOST, RCON_PORT, passwd=RCON_PASSWORD) as client:
            return {'ok': True, 'result': client.run(command)}
    except Exception as e:
        return {'ok': False, 'error': str(e)}

def rcon_gamemode(gamemode):
    cmd = GAMEMODES.get(gamemode)
    if not cmd:
        return
    for part in cmd.split(';'):
        part = part.strip()
        if part:
            rcon_command(part)

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
    return jsonify({
        'maps': {name: mtype for name, (cmd, mtype) in MAPS.items()},
        'gamemodes': list(GAMEMODES.keys()),
        'mode_maps': {mode: list(maps) for mode, maps in MODE_MAPS.items()},
        'workshop': {k: list(v.keys()) for k, v in WORKSHOP_MAPS.items()}
    })

@app.route('/api/map', methods=['POST'])
@login_required
def change_map():
    data = request.json or {}
    name = data.get('map')
    gamemode = data.get('gamemode', 'Casual')
    if name not in MAPS:
        return jsonify({'error': 'Unknown map'}), 400
    rcon_gamemode(gamemode)
    r = rcon_command(f'map {MAPS[name][0]}')
    return jsonify(r)

@app.route('/api/community_map', methods=['POST'])
@login_required
def community_map():
    data = request.json or {}
    name = data.get('map', '').strip()
    gamemode = data.get('gamemode', 'Casual')
    if not name or not re.match(r'^[a-zA-Z0-9_]+$', name):
        return jsonify({'ok': False, 'error': 'Invalid map name'}), 400
    rcon_gamemode(gamemode)
    r = rcon_command(f'map {name}')
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
    rcon_gamemode(gamemode)
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
