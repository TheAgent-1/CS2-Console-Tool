import platform
import os
import pygetwindow as gw
import pyautogui
import time
import subprocess
from flask import Flask, request, jsonify
import requests
import threading
from waitress import serve
import socket
from tkinter import messagebox

app = Flask(__name__)
logged_user = ""
try:
    hostIP:str = socket.gethostbyname('server')
except socket.gaierror:
    print("No server on network, switching to external IP")
    hostIP:str = "121.73.190.141"
port = '63251'

class CS2:
    def start_flask1(username):
        if username == "server":
            # Start the server in a separate thread
            server_thread = threading.Thread(target=CS2.start_flask2)
            server_thread.daemon = True  # This makes sure the server thread will close when the main program exits
            server_thread.start()
        else:
            global logged_user
            logged_user = username
            print(logged_user)

    def start_flask2():
        #app.run(host=host, port=port, threading=True)
        serve(app, host=hostIP, port=port)

    @app.route('/submit', methods=['POST'])
    def receive_data():
        # Get the JSON data from the request
        data = request.json

        # Extract username and string from the JSON data
        username = data.get("username")
        user_string = data.get("string")

        # Check if the order is preserved
        param_order = list(data.keys())

        # Check if both fields are provided
        if not username or not user_string:
            return jsonify({'error': 'Both username and string are required!'}), 400
        
        if param_order.index("username") > param_order.index("string"):
            print('Bad data sent')
            return jsonify({'error': 'Bad data sent'}), 400

        # Return a response with the received data
        CS2.send_command_to_CS2(user_string)
        return jsonify({'message': 'Data received successfully', "username": username, "string": user_string}), 200

    def find_on_desktop(file_or_folder_name):
        # Get the user's home directory
        home_dir = os.path.expanduser("~")

        # Construct the path to the traditional desktop
        desktop_path = os.path.join(home_dir, "Desktop")

        # Construct the path to the OneDrive desktop (assuming default setup)
        onedrive_path = os.path.join(home_dir, "OneDrive", "Desktop")

        # List of potential desktop paths to check
        desktop_paths = [desktop_path, onedrive_path]

        # Try each potential path and check if the file or folder exists
        for path in desktop_paths:
            target_path = os.path.join(path, file_or_folder_name)
            if os.path.exists(target_path):
                print(f"{file_or_folder_name} found on the desktop at: {target_path}")

                return

        print(f"{file_or_folder_name} not found on the desktop.")

    def get_path(file_or_folder_name):
        # Get the user's home directory
        home_dir = os.path.expanduser("~")

        # Construct the path to the traditional desktop
        desktop_path = os.path.join(home_dir, "Desktop")

        # Construct the path to the OneDrive desktop (assuming default setup)
        onedrive_path = os.path.join(home_dir, "OneDrive", "Desktop")

        # List of potential desktop paths to check
        desktop_paths = [desktop_path, onedrive_path]

        # Try each potential path and check if the file or folder exists
        for path in desktop_paths:
            target_path = os.path.join(path, file_or_folder_name)
            if os.path.exists(target_path):
                print(f"{file_or_folder_name} found on the desktop at: {target_path}")

                return target_path

        print(f"{file_or_folder_name} not found on the desktop.")

    def open(path):
        try:
            subprocess.run(path, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running batch file: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def send_command_to_CS2(command):
        # is the tool running on the server
        device_name = socket.gethostname()
        if platform.system() == "Windows":
            print(device_name)  
        
    
        if device_name == "server": # the tool is running on the server, send commands direct
            window_title = "Counter-Strike 2"
            window_title2 = "Untitled"

            if command == "!START":
                CS2.start_server()
                return

            if command == "!START -U":
                CS2.update_start_server()
                return

            if command == "!STOP":
                CS2.stop_server()
                return

            cs2_window = gw.getWindowsWithTitle(window_title)
            if not cs2_window:
                print(f"Window with title '{window_title}' not found.")
                return
        
            cs2_window = cs2_window[0]
            cs2_window.activate()
            pyautogui.typewrite(command, interval=0.05)
            pyautogui.press('enter')
            time.sleep(0.5)

        if device_name != "server": # the tool is running on a client computer, send commands over HTTP
            url = "http://" + hostIP + ":" + port + "/submit"
            data = {
                "username": logged_user,
                "string": command
            }

            # Send a POST request with the JSON data
            try:
                response = requests.post(url, json=data, timeout=5)
            except requests.exceptions.RequestException as e:
                messagebox.showerror("Error from server", f"Could not contact server\n\nCheck server for running tool\n\nError: {e}")
                return

            # Check the response from the server
            if response.status_code == 200:
                print('Message sent successfully!')
                print('Server response:', response.json())
                return
            if response.status_code == 500:
                messagebox.showerror("Error from server", 'Server is overloaded, Please restart Server-side tool')
                return
            else:
                messagebox.showerror("Error from server", f'Code: {response.status_code} \nMessage: {response.text} \nData: {data}')
                print('Failed to send message. Status code:', response.status_code)
                print('Error message:', response.text)
                print('Data contains:', data)
                return

    def bot(task):
        match task:
            case "kick":
                CS2.send_command_to_CS2("bot_kick")
            case "add_CT":
                CS2.send_command_to_CS2("bot_add_ct")
            case "add_T":
                CS2.send_command_to_CS2("bot_add_t")
            case "give_AI":
                CS2.send_command_to_CS2("exec bot_ai.cfg")

    def gamemode(mode):
        match mode:
            case "casual":
                CS2.send_command_to_CS2("game_alias casual")
            case "competitive":
                CS2.send_command_to_CS2("game_alias competitive")
            case "wingman":
                CS2.send_command_to_CS2("game_alias wingman")
            case "flyingscouts":
                CS2.send_command_to_CS2("game_type 0; game_mode 0; sv_skirmish_id 3")
            case "armsrace":
                CS2.send_command_to_CS2("game_type 1; game_mode 0; sv_skirmish_id 10")
            case "demolition":
                CS2.send_command_to_CS2("game_type 1; game_mode 1; sv_skirmish_id 11")
            case "deathmatch":
                CS2.send_command_to_CS2("game_alias deathmatch")
            case "guardian":
                CS2.send_command_to_CS2("game_type 4; game_mode 0")
            case "1PM":
                CS2.send_command_to_CS2("mp_weapons_max_gun_purchases_per_weapon_per_match -1")

    def change_map(map):
        match map:
            case "Ancient":
                CS2.send_command_to_CS2("changelevel de_ancient")
            case "Anubis":
                CS2.send_command_to_CS2("changelevel de_anubis")
            case "Dust2":
                CS2.send_command_to_CS2("changelevel de_dust2")
            case "Inferno":
                CS2.send_command_to_CS2("changelevel de_inferno")
            case "Italy":
                CS2.send_command_to_CS2("changelevel cs_italy")
            case "Mirage":
                CS2.send_command_to_CS2("changelevel de_mirage")
            case "Nuke":
                CS2.send_command_to_CS2("changelevel de_nuke")
            case "Office":
                CS2.send_command_to_CS2("changelevel cs_office")
            case "Overpass":
                CS2.send_command_to_CS2("changelevel de_overpass")
            case "Vertigo":
                CS2.send_command_to_CS2("changelevel de_vertigo")
            case "Baggage":
                CS2.send_command_to_CS2("changelevel ar_baggage")
            case "Shoots":
                CS2.send_command_to_CS2("changelevel ar_shoots")

    def workshop(WS_map):
        match WS_map:

            #BOMB
            case "foroglioCasual":
                CS2.send_command_to_CS2("game_alias casual")
                CS2.send_command_to_CS2("host_workshop_map 3132854332")
            case "assemblyCasual":
                CS2.send_command_to_CS2("game_alias casual")
                CS2.send_command_to_CS2("host_workshop_map 3071005299")
            case "blackgoldCasual":
                CS2.send_command_to_CS2("game_alias casual")
                CS2.send_command_to_CS2("host_workshop_map 3075012302")
            case "lakeCasual":
                CS2.send_command_to_CS2("game_alias casual")
                CS2.send_command_to_CS2("host_workshop_map 3070563536")
            case "bankCasual":
                CS2.send_command_to_CS2("game_alias casual")
                CS2.send_command_to_CS2("host_workshop_map 3070581293")
            case "bikinibottomCasual":
                CS2.send_command_to_CS2("game_alias casual")
                CS2.send_command_to_CS2("host_workshop_map 3204870970")
            case "planeCasual":
                CS2.send_command_to_CS2("game_alias casual")
                CS2.send_command_to_CS2("host_workshop_map 3217247541")
            case "stmarcCasual":
                CS2.send_command_to_CS2("game_alias casual")
                CS2.send_command_to_CS2("host_workshop_map 3070562370")
            case "sugarcaneCasual":
                CS2.send_command_to_CS2("game_alias casual")
                CS2.send_command_to_CS2("host_workshop_map 3070579459")
            case "astraCasual":
                CS2.send_command_to_CS2("game_alias casual")
                CS2.send_command_to_CS2("host_workshop_map 3083296922")
            case "maginotCasual":
                CS2.send_command_to_CS2("game_alias casual")
                CS2.send_command_to_CS2("host_workshop_map 3195399109")
            case "palaisCasual":
                CS2.send_command_to_CS2("game_alias casual")
                CS2.send_command_to_CS2("host_workshop_map 3257582863")
            case "omahabeachCasual":
                CS2.send_command_to_CS2("game_alias casual")
                CS2.send_command_to_CS2("host_workshop_map 3148007939")
            case "trainCasual":
                CS2.send_command_to_CS2("game_alias casual")
                CS2.send_command_to_CS2("host_workshop_map 3070284539")
            case "atticCasual":
                CS2.send_command_to_CS2("game_alias casual")
                CS2.send_command_to_CS2("host_workshop_map 3305148449")
            case "themetroCasual":
                CS2.send_command_to_CS2("game_alias casual")
                CS2.send_command_to_CS2("host_workshop_map 3326236589")
            case "cacheCasual":
                CS2.send_command_to_CS2("game_alias casual")
                CS2.send_command_to_CS2("host_workshop_map 3328271311")
            case "incaCasual":
                CS2.send_command_to_CS2("game_alias casual")
                CS2.send_command_to_CS2("host_workshop_map 3325387224")
            case "sparityCasual":
                CS2.send_command_to_CS2("game_alias casual")
                CS2.send_command_to_CS2("host_workshop_map 3317923634")
            case "basaltCasual":
                CS2.send_command_to_CS2("game_alias casual")
                CS2.send_command_to_CS2("host_workshop_map 3329258290")
            case "zooCasual":
                CS2.send_command_to_CS2("game_alias casual")
                CS2.send_command_to_CS2("host_workshop_map 3101352333")
            case "tuscanCasual":
                CS2.send_command_to_CS2("game_alias casual")
                CS2.send_command_to_CS2("host_workshop_map 3267671493")   
            case "rainfallCasual":
                CS2.send_command_to_CS2("game_alias casual")
                CS2.send_command_to_CS2("host_workshop_map 3265650949")
            case "lighthouseCasual":
                CS2.send_command_to_CS2("game_alias casual")
                CS2.send_command_to_CS2("host_workshop_map 3342529755")
            case "RefuseCasual":
                CS2.send_command_to_CS2("game_alias casual")
                CS2.send_command_to_CS2("host_workshop_map 3294609675")



            #HOSTAGE
            case "rushCasual":
                CS2.send_command_to_CS2("game_alias casual")
                CS2.send_command_to_CS2("host_workshop_map 3077752384")
            case "safehouseCasual":
                CS2.send_command_to_CS2("game_alias casual")
                CS2.send_command_to_CS2("host_workshop_map 3070550406")
            case "minecraftCasual":
                CS2.send_command_to_CS2("game_alias casual")
                CS2.send_command_to_CS2("host_workshop_map 3095875614")
            case "damCasual":
                CS2.send_command_to_CS2("game_alias casual")
                CS2.send_command_to_CS2("host_workshop_map 3072481684")
            case "assaultCasual":
                CS2.send_command_to_CS2("game_alias casual")
                CS2.send_command_to_CS2("host_workshop_map 3079872050")
            case "rainbow6Casual":
                CS2.send_command_to_CS2("game_alias casual")
                CS2.send_command_to_CS2("host_workshop_map 3115452448")
            case "militiaCasual":
                CS2.send_command_to_CS2("game_alias casual")
                CS2.send_command_to_CS2("host_workshop_map 3202169771")
            case "hijackCasual":
                CS2.send_command_to_CS2("game_alias casual")
                CS2.send_command_to_CS2("host_workshop_map 3310206718")
            case "climbCasual":
                CS2.send_command_to_CS2("game_alias casual")
                CS2.send_command_to_CS2("host_workshop_map 3319649237")
            case "agencyCasual":
                CS2.send_command_to_CS2("game_alias casual")
                CS2.send_command_to_CS2("host_workshop_map 3339983232")
            case "paris2024Casual":
                CS2.send_command_to_CS2("game_alias casual")
                CS2.send_command_to_CS2("host_workshop_map 3344069159")

            

            #ARMSRACE
            case "lunacyArms":
                CS2.gamemode("armsrace")
                CS2.send_command_to_CS2("host_workshop_map 3070560242")
            case "monasteryArms":
                CS2.gamemode("armsrace")
                CS2.send_command_to_CS2("host_workshop_map 3070547153")
            case "stmarcArms":
                CS2.gamemode("armsrace")
                CS2.send_command_to_CS2("host_workshop_map 3070562370")
            case "stairsArms":
                CS2.gamemode("armsrace")
                CS2.send_command_to_CS2("host_workshop_map 3264733671")
            case "churchesArms":
                CS2.gamemode("armsrace")
                CS2.send_command_to_CS2("host_workshop_map 3070291913")
            case "pooldayArms":
                CS2.gamemode("armsrace")
                CS2.send_command_to_CS2("host_workshop_map 3070923343")
            case "speedballArms":
                CS2.gamemode("armsrace")
                CS2.send_command_to_CS2("host_workshop_map 3111527644")
            


            
            #DEATHMATCH
            case "omahabeachDeathmatch":
                CS2.gamemode("deathmatch")
                CS2.send_command_to_CS2("host_workshop_map 3148007939")
            case "astraDeathmatch":
                CS2.gamemode("deathmatch")
                CS2.send_command_to_CS2("host_workshop_map 3083296922")
            case "haloDeathmatch":
                CS2.gamemode("deathmatch")
                CS2.send_command_to_CS2("host_workshop_map 3255907412")
            case "breadwindowDeathmatch":
                CS2.send_command_to_CS2("game_alias deathmatch")
                CS2.send_command_to_CS2("host_workshop_map 3371417956")
            case "eternalDeathmatch":
                CS2.gamemode("deathmatch")
                CS2.send_command_to_CS2("host_workshop_map 3094002407")
            case "mansionDeathmatch":
                CS2.gamemode("deathmatch")
                CS2.send_command_to_CS2("host_workshop_map 3080114822")
            case "airealityDeathmatch":
                CS2.gamemode("deathmatch")
                CS2.send_command_to_CS2("host_workshop_map 3105649124")
            case "lighthouseDeathmatch":
                CS2.gamemode("deathmatch")
                CS2.send_command_to_CS2("host_workshop_map 3342529755")



            #REMOVED
            #case "planeArms":
                #CS2.gamemode("armsrace")
                #CS2.send_command_to_CS2("host_workshop_map 3217247541")
            #case "minimirage":
                #CS2.send_command_to_CS2("game_alias casual")
                #CS2.send_command_to_CS2("host_workshop_map 3099519038")
            #case "rustdeath":
                #CS2.gamemode("deathmatch")
                #CS2.send_command_to_CS2("host_workshop_map 3131645522")
            #case "2towers":
                #CS2.send_command_to_CS2("host_workshop_map 3160551327")
            #case "nuketown":
                #CS2.send_command_to_CS2("game_alias casual")
                #CS2.send_command_to_CS2("host_workshop_map 3133577140")
            #case "glass":
                #CS2.send_command_to_CS2("game_alias casual")
                #CS2.send_command_to_CS2("host_workshop_map 3089842427")
            #case "chickens":
                #CS2.send_command_to_CS2("game_alias casual")
                #CS2.send_command_to_CS2("host_workshop_map 3072401024")
            #case "turbulence":
                #CS2.send_command_to_CS2("game_alias casual")
                #CS2.send_command_to_CS2("host_workshop_map 3307334950")
            #case "invasionarms":
                #CS2.gamemode("armsrace")
                #CS2.send_command_to_CS2("host_workshop_map 3307925166")
            #case "mirage45":
                #CS2.send_command_to_CS2("game_alias casual")
                #CS2.send_command_to_CS2("host_workshop_map 3270516952")
            #case "futsal":
                #CS2.send_command_to_CS2("game_alias casual")
                #CS2.send_command_to_CS2("host_workshop_map 3293224257")
              
            
            
            
            
                

    def respawn(option):
        match option:
            case "CT_YES":
                CS2.send_command_to_CS2("mp_respawn_on_death_ct 1")
            case "CT_NO":
                CS2.send_command_to_CS2("mp_respawn_on_death_ct 0")
            case "T_YES":
                CS2.send_command_to_CS2("mp_respawn_on_death_t 1")
            case "T_NO":
                CS2.send_command_to_CS2("mp_respawn_on_death_t 0")

    def kick(player):
        CS2.send_command_to_CS2("sv_kick_ban_duration 3")
        CS2.send_command_to_CS2("kick Melben")

    def ban(player):
        import random
        randint = random.randint(1, 10)
        #print("banid {} 1573991913".format(randint))
        CS2.send_command_to_CS2("banid {} 1573991913".format(randint))

    def start_server():
        import secrets
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        project_folder = "CS2_tool"
        subfolder_name = "startFiles"

        folder_path = os.path.join(desktop_path, project_folder, subfolder_name)
        print(f"Folder path: {folder_path}")

        StartFiles = [f for f in os.listdir(folder_path)]
        print(StartFiles)
        randomfile = secrets.choice(StartFiles)
        randomfile_path = os.path.join(folder_path, randomfile)
        print(randomfile_path)
        try:
            subprocess.Popen([randomfile_path])
            print(f"Successfully executed: {randomfile_path}")
        except Exception as e:
            print(f"Error executing {randomfile_path}: {e}")
        
    def update_start_server():
        try:
            subprocess.Popen("C:/Users/server/Desktop/CS2_tool/BigBrotherUpdate.bat")
        except Exception as e:
            print(f"Error executing update script: {e}")

    def update_IP():
        try:
            import requests

            duck_token = '1bf2b997-5e79-4061-b51d-d2d49a40b076'
            domain = 'croul'

            ip = requests.get('https://api.ipify.org').text
            print('my ip: {}'.format(ip))

            url = 'https://duckdns.org/update/' + domain + '/' + duck_token + '/' + ip

            duck = requests.get(url).text
            print(duck)
            return duck
        except requests.exceptions.RequestException as e:
            print(f"Error updating IP: {e}")
            return None

    def stop_server():
        #CS2.send_command_to_CS2("sv_shutdown")
        subprocess.call("TASKKILL /F /IM cs2.exe", shell=True)