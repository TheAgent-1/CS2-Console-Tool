import os
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
from CS2Copy import CS2


window = tk.Tk()
result_variable = tk.StringVar()

base_path = os.path.join(os.path.dirname(__file__), "assets")

Ancient = PhotoImage(file=os.path.join(base_path, "Ancient.png")).subsample(2, 2)
Anubis = PhotoImage(file=os.path.join(base_path, "Anubis.png")).subsample(2, 2)
Dust2 = PhotoImage(file=os.path.join(base_path, "Dust2.png")).subsample(2, 2)
Inferno = PhotoImage(file=os.path.join(base_path, "Inferno.png")).subsample(2, 2)
Italy = PhotoImage(file=os.path.join(base_path, "Italy.png")).subsample(2, 2)
Mirage = PhotoImage(file=os.path.join(base_path, "Mirage.png")).subsample(2, 2)
Nuke = PhotoImage(file=os.path.join(base_path, "Nuke.png")).subsample(2, 2)
Office = PhotoImage(file=os.path.join(base_path, "Office.png")).subsample(2, 2)
Overpass = PhotoImage(file=os.path.join(base_path, "Overpass.png")).subsample(2, 2)
Vertigo = PhotoImage(file=os.path.join(base_path, "Vertigo.png")).subsample(2, 2)
Baggage = PhotoImage(file=os.path.join(base_path, "Baggage.png")).subsample(9, 9)
Shoots = PhotoImage(file=os.path.join(base_path, "Shoots.png")).subsample(9, 9)


def login():
    window.title("CS2 GUI")
    window.geometry("620x600") # Add this line to set the window size

    for widget in window.winfo_children():
        widget.destroy()

    login_frame = tk.Frame(window)
    login_frame.pack(pady=50)

    label_username = tk.Label(login_frame, text="Username:")
    label_username.pack()

    entry_username = tk.Entry(login_frame)
    entry_username.pack()

    label_password = tk.Label(login_frame, text="Password:")
    label_password.pack()

    entry_password = tk.Entry(login_frame, show="*")
    entry_password.pack()

    login_button = tk.Button(login_frame, text="Login", command=lambda: login_check(entry_username.get(), entry_password.get()))
    login_button.pack(pady=10)
    window.mainloop()

def login_check(username, password):
    users = {
    'server': 'server',
    'Jacob': 'Gh0s7!',
    'Chris': 'Chris',
    'Jonno': 'Jonno13',
    'test': ''
    }

    if username in users and users[username] == password:
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
        CS2.start_flask1(username)
        main()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


def main():
    
    window.title("CS2 GUI")
    window.geometry("620x800") # Add this line to set the window size

    for widget in window.winfo_children():
        widget.destroy()

    bot_commands_button = tk.Button(window, text="Bot Commands", command=bot_commands)
    bot_commands_button.pack()

    game_mode_button = tk.Button(window, text="GameMode", command=game_mode)
    game_mode_button.pack()

    change_map_button = tk.Button(window, text="Change Map", command=change_map)
    change_map_button.pack()

    workshop_map_button = tk.Button(window, text="Workshop Maps", command=workshop_map)
    workshop_map_button.pack()

    respawn_on_death_button = tk.Button(window, text="Respawn On Death", command=respawn_on_death)
    respawn_on_death_button.pack()

    kick_button = tk.Button(window, text="3 minute ban", command=kick_player)
    kick_button.pack()

    startup_button = tk.Button(window, text="Start Server", command=startup)
    startup_button.pack()

    shutdown_button = tk.Button(window, text="Shutdown", command=shutdown)
    shutdown_button.pack()

    logout_button = tk.Button(window, text="Log Out", command=login)
    logout_button.pack()

    

def bot_commands():
    for widget in window.winfo_children():
        widget.destroy()

    Back_button = tk.Button(window, text="Back", command=main)
    Back_button.pack()

    bot_kick_button = tk.Button(window, text="Kick Bots", command=lambda: CS2.bot("kick"))
    bot_kick_button.pack()

    bot_addCT_button = tk.Button(window, text="Add CT Bot", command=lambda: CS2.bot("add_CT"))
    bot_addCT_button.pack()

    bot_addT_button = tk.Button(window, text="Add T Bot", command=lambda: CS2.bot("add_T"))
    bot_addT_button.pack()

    bot_giveAI_button = tk.Button(window, text="Give AI to Bots", command=lambda: CS2.bot("give_AI"))
    bot_giveAI_button.pack()

def game_mode():
    for widget in window.winfo_children():
        widget.destroy()

    Back_button = tk.Button(window, text="Back", command=main)
    Back_button.pack()

    Casual_button = tk.Button(window, text="Casual", command=lambda: CS2.gamemode("casual"))
    Casual_button.pack()

    Competitive_button = tk.Button(window, text="Competitive", command=lambda: CS2.gamemode("competitive"))
    Competitive_button.pack()

    Wingman_button = tk.Button(window, text="Wingman", command=lambda: CS2.gamemode("wingman"))
    Wingman_button.pack()

    Flyingscouts_Button = tk.Button(window, text="Flying Scoutsman", command=lambda: CS2.gamemode("flyingscouts"))
    Flyingscouts_Button.pack()

    ArmsRace_button = tk.Button(window, text="Arms Race", command=lambda: CS2.gamemode("armsrace"))
    ArmsRace_button.pack()

    Demolition_button = tk.Button(window, text="Demolition", command=lambda: CS2.gamemode("demolition"))
    Demolition_button.pack()

    Deathmatch_button = tk.Button(window, text="Deathmatch", command=lambda: CS2.gamemode("deathmatch"))
    Deathmatch_button.pack()

    Guardian_button = tk.Button(window, text="Guardian", command=lambda: CS2.gamemode("guardian"))
    Guardian_button.pack()

    Custom_button = tk.Button(window, text="Custom", command=lambda: custom_setup())
    Custom_button.pack()

    OnePerMatch_button = tk.Button(window, text="1 per match", command=lambda:CS2.gamemode("1PM"))
    OnePerMatch_button.pack()

def change_map():
    for widget in window.winfo_children():
        widget.destroy()

    Back_button = tk.Button(window, text="Back", command=main)
    Back_button.grid(row=0, column=3)
    
    # ROW 1
    Ancient_button = tk.Button(window, text="Ancient", image=Ancient, command=lambda: CS2.change_map("Ancient"))
    Ancient_button.grid(row=1, column=1)

    Anubis_button = tk.Button(window, text="Anubis", image=Anubis, command=lambda: CS2.change_map("Anubis"))
    Anubis_button.grid(row=1, column=2)

    Dust2_button = tk.Button(window, text="Dust2", image=Dust2, command=lambda: CS2.change_map("Dust2"))
    Dust2_button.grid(row=1, column=3)

    Inferno_button = tk.Button(window, text="Inferno", image=Inferno, command=lambda: CS2.change_map("Inferno"))
    Inferno_button.grid(row=1, column=4)

    Italy_button = tk.Button(window, text="Italy", image=Italy, command=lambda: CS2.change_map("Italy"))
    Italy_button.grid(row=1, column=5)

    # ROW 2
    Mirage_button = tk.Button(window, text="Mirage", image=Mirage, command=lambda: CS2.change_map("Mirage"))
    Mirage_button.grid(row=2, column=1)

    Nuke_button = tk.Button(window, text="Nuke", image=Nuke, command=lambda: CS2.change_map("Nuke"))
    Nuke_button.grid(row=2, column=2)

    Office_button = tk.Button(window, text="Office", image=Office, command=lambda: CS2.change_map("Office"))
    Office_button.grid(row=2, column=3)

    Overpass_button = tk.Button(window, text="Overpass", image=Overpass, command=lambda: CS2.change_map("Overpass"))
    Overpass_button.grid(row=2, column=4)

    Vertigo_button = tk.Button(window, text="Vertigo", image=Vertigo, command=lambda: CS2.change_map("Vertigo"))
    Vertigo_button.grid(row=2, column=5)

    # ROW 3
    Baggage_button = tk.Button(window, text="Baggage", image=Baggage, command=lambda: CS2.change_map("Baggage"))
    Baggage_button.grid(row=3, column=1)

    Shoots_button = tk.Button(window, text="Shoots", image=Shoots, command=lambda: CS2.change_map("Shoots"))
    Shoots_button.grid(row=3, column=2)

def workshop_map():
    #Bomb - column=0
    #Hostage - column=1
    #arms - column=3
    #death- column=4
    

    for widget in window.winfo_children():
        widget.destroy()

    Back_button = tk.Button(window, text="Back", command=main)
    Back_button.grid(row=0, column=2)



    Bomb_frame = tk.Frame(window, bg="lightblue", padx=10, pady=10)
    Bomb_frame.grid(row=1, column=0, rowspan=26, sticky="nsew")

    Hostage_frame = tk.Frame(window, bg="lightblue", padx=10, pady=10)
    Hostage_frame.grid(row=1, column=1, rowspan=26, sticky="nsew")

    Armsrace_frame = tk.Frame(window, bg="lightblue", padx=10, pady=10)
    Armsrace_frame.grid(row=1, column=3, rowspan=26, sticky="nsew")

    Deathmatch_frame = tk.Frame(window, bg="lightblue", padx=10, pady=10)
    Deathmatch_frame.grid(row=1, column=4, rowspan=26, sticky="nsew")

    Bomb_label = tk.Label(Bomb_frame, text="Bomb", bg="lightblue", font=("Arial", 12, "bold"))
    Bomb_label.pack()

    Hostage_label = tk.Label(Hostage_frame, text="Hostage", bg="lightblue", font=("Arial", 12, "bold"))
    Hostage_label.pack()

    Armsrace_label = tk.Label(Armsrace_frame, text="Armsrace", bg="lightblue", font=("Arial", 12, "bold"))
    Armsrace_label.pack()

    Deathmatch_label = tk.Label(Deathmatch_frame, text="Deathmatch", bg="lightblue", font=("Arial", 12, "bold"))
    Deathmatch_label.pack()

    

    #BOMB
    WS_foroglioCasual_button = tk.Button(Bomb_frame, text="Casual Foroglio", command=lambda: CS2.workshop("foroglioCasual"))
    WS_foroglioCasual_button.pack()

    WS_assemblyCasual_button = tk.Button(Bomb_frame, text="Casual Assembly", command=lambda: CS2.workshop("assemblyCasual"))
    WS_assemblyCasual_button.pack()

    WS_blackgoldCasual_button = tk.Button(Bomb_frame, text="Casual Black Gold", command=lambda: CS2.workshop("blackgoldCasual"))
    WS_blackgoldCasual_button.pack()

    WS_lakeCasual_button = tk.Button(Bomb_frame, text="Casual lake", command=lambda: CS2.workshop("lakeCasual"))
    WS_lakeCasual_button.pack()

    WS_bankCasual_button = tk.Button(Bomb_frame, text="Casual Bank", command=lambda: CS2.workshop("bankCasual"))
    WS_bankCasual_button.pack()

    WS_bikinibottomCasual_button = tk.Button(Bomb_frame, text="Casual BikiniBottom", command=lambda: CS2.workshop("bikinibottomCasual"))
    WS_bikinibottomCasual_button.pack()

    WS_planeCasual_button = tk.Button(Bomb_frame, text="Casual Plane", command=lambda: CS2.workshop("planeCasual"))
    WS_planeCasual_button.pack()

    WS_stmarcCasual_button = tk.Button(Bomb_frame, text="Casual StMarc", command=lambda: CS2.workshop("stmarcCasual"))
    WS_stmarcCasual_button.pack()

    WS_sugarcaneCasual_button = tk.Button(Bomb_frame, text="Casual SugarCane", command=lambda: CS2.workshop("sugarcaneCasual"))
    WS_sugarcaneCasual_button.pack()

    WS_astraCasual_button = tk.Button(Bomb_frame, text="Casual Astra", command=lambda: CS2.workshop("astraCasual"))
    WS_astraCasual_button.pack()

    WS_maginotCasual_button = tk.Button(Bomb_frame, text="Casual Maginot", command=lambda: CS2.workshop("maginotCasual"))
    WS_maginotCasual_button.pack()
    
    WS_palaisCasual_button = tk.Button(Bomb_frame, text="Casual Palais", command=lambda: CS2.workshop("palaisCasual"))
    WS_palaisCasual_button.pack()

    WS_omahabeachCasual_button = tk.Button(Bomb_frame, text="Casual OmhaBeach", command=lambda: CS2.workshop("omahabeachCasual"))
    WS_omahabeachCasual_button.pack()

    WS_trainCasual_button = tk.Button(Bomb_frame, text="Casual Train", command=lambda: CS2.workshop("trainCasual"))
    WS_trainCasual_button.pack()

    WS_atticCasual_button = tk.Button(Bomb_frame, text="Casual Attic", command=lambda: CS2.workshop("atticCasual"))
    WS_atticCasual_button.pack()

    WS_themetroCasual_button = tk.Button(Bomb_frame, text="Casual The Metro", command=lambda: CS2.workshop("themetroCasual"))
    WS_themetroCasual_button.pack()

    WS_cacheCasual_button = tk.Button(Bomb_frame, text="Casual Cache", command=lambda: CS2.workshop("cacheCasual"))
    WS_cacheCasual_button.pack()

    WS_incaCasual_button = tk.Button(Bomb_frame, text="Casual Inca", command=lambda: CS2.workshop("incaCasual"))
    WS_incaCasual_button.pack()
    
    WS_sparityCasual_button = tk.Button(Bomb_frame, text="Casual Sparity", command=lambda: CS2.workshop("sparityCasual"))
    WS_sparityCasual_button.pack()

    WS_basaltCasual_button = tk.Button(Bomb_frame, text="Casual Basalt", command=lambda: CS2.workshop("basaltCasual"))
    WS_basaltCasual_button.pack()

    WS_zooCasual_button = tk.Button(Bomb_frame, text="Casual Zoo", command=lambda: CS2.workshop("zooCasual"))
    WS_zooCasual_button.pack()

    WS_tuscanCasual_button = tk.Button(Bomb_frame, text="Casual Tuscan", command=lambda: CS2.workshop("tuscanCasual"))
    WS_tuscanCasual_button.pack()

    WS_rainfallCasual_button = tk.Button(Bomb_frame, text="Casual Rainfall", command=lambda: CS2.workshop("rainfallCasual"))
    WS_rainfallCasual_button.pack()

    WS_lighthouseCasual_button = tk.Button(Bomb_frame, text="Casual Lighthouse", command=lambda: CS2.workshop("lighthouseCasual"))
    WS_lighthouseCasual_button.pack()



    #HOSTAGE
    WS_rushCasual_button = tk.Button(Hostage_frame, text="Casual Rush", command=lambda: CS2.workshop("rushCasual"))
    WS_rushCasual_button.pack()

    WS_safehouseCasual_button = tk.Button(Hostage_frame, text="Casual Safehouse", command=lambda: CS2.workshop("safehouseCasual"))
    WS_safehouseCasual_button.pack()

    WS_minecraftCasual_button = tk.Button(Hostage_frame, text="Casual Minecraft", command=lambda: CS2.workshop("minecraftCasual"))
    WS_minecraftCasual_button.pack()

    WS_damCasual_button = tk.Button(Hostage_frame, text="Casual Dam", command=lambda: CS2.workshop("damCasual"))
    WS_damCasual_button.pack()

    WS_assaultCasual_button = tk.Button(Hostage_frame, text="Casual Assault", command=lambda: CS2.workshop("assaultCasual"))
    WS_assaultCasual_button.pack()

    WS_rainbow6Casual_button = tk.Button(Hostage_frame, text="Casual Rainbow6", command=lambda: CS2.workshop("rainbow6Casual"))
    WS_rainbow6Casual_button.pack()

    WS_militiaCasual_button = tk.Button(Hostage_frame, text="Casual Militia", command=lambda: CS2.workshop("militiaCasual"))
    WS_militiaCasual_button.pack()

    WS_hijackCasual_button = tk.Button(Hostage_frame, text="Casual HiJack", command=lambda: CS2.workshop("hijackCasual"))
    WS_hijackCasual_button.pack()

    WS_climbCasual_button = tk.Button(Hostage_frame, text="Casual Climb", command=lambda: CS2.workshop("climbCasual"))
    WS_climbCasual_button.pack()

    WS_agencyCasual_button = tk.Button(Hostage_frame, text="Casual Agency", command=lambda: CS2.workshop("agencyCasual"))
    WS_agencyCasual_button.pack()

    WS_paris2024Casual_button = tk.Button(Hostage_frame, text="Casual Paris2024", command=lambda: CS2.workshop("paris2024Casual"))
    WS_paris2024Casual_button.pack()



    #ARMSRACE
    WS_lunacyArms_button = tk.Button(Armsrace_frame, text="Arms Lunacy", command=lambda: CS2.workshop("lunacyArms"))
    WS_lunacyArms_button.pack()

    WS_monasteryArms_button = tk.Button(Armsrace_frame, text="Arms Monastery", command=lambda: CS2.workshop("monasteryArms"))
    WS_monasteryArms_button.pack()

    WS_stmarcArms_button = tk.Button(Armsrace_frame, text="Arms StMarc", command=lambda: CS2.workshop("stmarcArms"))
    WS_stmarcArms_button.pack()

    WS_stairsarms_button = tk.Button(Armsrace_frame, text="Arms Stairs", command=lambda: CS2.workshop("stairsArms"))
    WS_stairsarms_button.pack()

    WS_churchesArms_button = tk.Button(Armsrace_frame, text="Arms Churches", command=lambda: CS2.workshop("churchesArms"))
    WS_churchesArms_button.pack()

    WS_pooldayArms_button = tk.Button(Armsrace_frame, text="Arms PoolDay", command=lambda: CS2.workshop("pooldayArms"))
    WS_pooldayArms_button.pack()

    WS_speedballArms_button = tk.Button(Armsrace_frame, text="Arms Speedball", command=lambda: CS2.workshop("speedballArms"))
    WS_speedballArms_button.pack()



    #DEATHMATCH
    WS_omahabeachDeathmatch_button = tk.Button(Deathmatch_frame, text="Deathmatch OmhaBeach", command=lambda: CS2.workshop("omahabeachDeathmatch"))
    WS_omahabeachDeathmatch_button.pack()
    
    WS_astraDeathmatch_button = tk.Button(Deathmatch_frame, text="Deathmatch Astra", command=lambda: CS2.workshop("astraDeathmatch"))
    WS_astraDeathmatch_button.pack()

    WS_haloDeathmatch_button = tk.Button(Deathmatch_frame, text="Deathmatch Halo", command=lambda: CS2.workshop("haloDeathmatch"))
    WS_haloDeathmatch_button.pack()

    WS_BreadwindowDeathmatch_button = tk.Button(Deathmatch_frame, text="Deathmatch Breadwindow", command=lambda: CS2.workshop("BreadwindowDeathmatch"))
    WS_BreadwindowDeathmatch_button.pack()

    WS_eternalDeathmatch_button = tk.Button(Deathmatch_frame, text="Deathmatch Eternal", command=lambda: CS2.workshop("eternalDeathmatch"))
    WS_eternalDeathmatch_button.pack()

    WS_mansionDeathmatch_button = tk.Button(Deathmatch_frame, text="Deathmatch Mansion", command=lambda: CS2.workshop("mansionDeathmatch"))
    WS_mansionDeathmatch_button.pack()
    
    WS_airealityDeathmatch_button = tk.Button(Deathmatch_frame, text="Deathmatch AIReality", command=lambda: CS2.workshop("airealityDeathmatch"))
    WS_airealityDeathmatch_button.pack()

    WS_lighthouseDeathmatch_button = tk.Button(Deathmatch_frame, text="Deathmatch Lighthouse", command=lambda: CS2.workshop("lighthouseDeathmatch"))
    WS_lighthouseDeathmatch_button.pack()

    WS_DollsHouseDeathmatch_button = tk.Button(Deathmatch_frame, text="Deathmatch DollsHouse", command=lambda: CS2.workshop("DollsHouseDeathmatch"))
    WS_DollsHouseDeathmatch_button.pack()


    #REMOVED
    #WS_planeArms_button = tk.Button(Armsrace_frame, text="Arms Plane", command=lambda: CS2.workshop("planeArms"))
    #WS_planeArms_button.pack()

    #WS_minimirage_button = tk.Button(window, text="Minimirage", command=lambda: CS2.workshop("minimirage"))
    #WS_minimirage_button.pack()

    #WS_rustdeath_button = tk.Button(window, text="Rust Deathmatch", command=lambda: CS2.workshop("rustdeath"))
    #WS_rustdeath_button.pack()

    #WS_2towers_button = tk.Button(window, text="Two Towers", command=lambda: CS2.workshop("2towers"))
    #WS_2towers_button.pack()

    #WS_nuketown_button = tk.Button(window, text="Nuketown", command=lambda: CS2.workshop("nuketown"))
    #WS_nuketown_button.pack()

    #WS_chickens_button = tk.Button(window, text="Bomb Chickens", command=lambda: CS2.workshop("chickens"))
    #WS_chickens_button.grid(row=16, column=0)

    #WS_glass_button = tk.Button(window, text="Casual Glass", command=lambda: CS2.workshop("glass"))
    #WS_glass_button.grid(row=20, column=0)

    #WS_turbulence_button = tk.Button(window, text="Flying Scotsman Turbulence", command=lambda: CS2.workshop("turbulence"))
    #WS_turbulence_button.grid(row=4, column=4)

    #WS_invasion_button = tk.Button(window, text="Arms Invasion", command=lambda: CS2.workshop("invasionarms"))
    #WS_invasion_button.grid(row=5, column=4)

    #WS_mirage45_button = tk.Button(window, text="Mirage 45", command=lambda: CS2.workshop("mirage45"))
    #WS_mirage45_button.grid(row=7, column=4)

    #WS_futsal_button = tk.Button(window, text="Football Futsal", command=lambda: CS2.workshop("futsal"))
    #WS_futsal_button.grid(row=10, column=4)

    

    

    

def respawn_on_death():
    for widget in window.winfo_children():
        widget.destroy()

    Back_button = tk.Button(window, text="Back", command=main)
    Back_button.pack()

    CTY_button = tk.Button(window, text="CT's respawn", command=lambda: CS2.respawn("CT_YES"))
    CTY_button.pack()

    CTN_button = tk.Button(window, text="CT's dont respawn", command=lambda: CS2.respawn("CT_NO"))
    CTN_button.pack()

    TY_button = tk.Button(window, text="T's respawn", command=lambda: CS2.respawn("T_YES"))
    TY_button.pack()

    TN_button = tk.Button(window, text="T's dont respawn", command=lambda: CS2.respawn("T_NO"))
    TN_button.pack()

def custom_setup():
    for widget in window.winfo_children():
        widget.destroy()

    
    mode_var = tk.StringVar(window)
    modes = ["", "casual", "competitive", "armsrace"]
    mode_var.set(modes[0])  # Set default value

    map_var = tk.StringVar(window)
    maps = ["", "Ancient", "Anubis", "Dust2", "Inferno", "Italy", "Mirage", "Nuke", "Office", "Overpass", "Vertigo", "Baggage", "Shoots"]
    map_var.set(modes[0])  # Set default value

    botAI_var = tk.StringVar(window)
    botAImodes = ["", "yes", "no"]
    botAI_var.set(modes[0])  # Set default value

    
    Back_button = tk.Button(window, text="Back", command=main).pack()

    mode_label = tk.Label(window, text="Gamemode:").pack()
    mode_select = tk.OptionMenu(window, mode_var, *modes).pack()
    map_label = tk.Label(window, text="Select Map:").pack()
    map_select = tk.OptionMenu(window, map_var, *maps).pack()
    botAI_label = tk.Label(window, text="Bot AI:").pack()
    botAI_select = tk.OptionMenu(window, botAI_var, *botAImodes).pack()
    wait_label = tk.Label(window, text="")
    Go_button = tk.Button(window, text="GO", command=lambda: custom_execute(mode_var.get(), map_var.get(), botAI_var.get(), wait_label)).pack()
    wait_label.pack()

def custom_execute(mode_var, map_var, AI_var, wait_label):
    import time
    print(mode_var)
    print(map_var)
    print(AI_var)
    wait_label.config(text="Please wait")
    CS2.gamemode(mode_var)
    CS2.change_map(map_var)

    if AI_var == "yes":
        
        time.sleep(10)
        CS2.bot("give_AI")
        wait_label.config(text="")



    #do button stuff here eg. if btn pressed get values

def kick_player():
    for widget in window.winfo_children():
        widget.destroy()

    Back_button = tk.Button(window, text="Back", command=main)
    Back_button.pack()

    kick = tk.Button(window, text="3 minute ban", command=lambda: CS2.kick("Melben"))
    kick.pack()

def startup():
    for widget in window.winfo_children():
        widget.destroy()

    Confirm_label = tk.Label(window, text="Start or Update?")
    Confirm_label.grid(row=1, column=1, pady=10)

    Startup_button = tk.Button(window, text="Start", command=lambda: CS2.send_command_to_CS2("!START"))
    Startup_button.grid(row=2, column=0, padx=5, sticky="e")

    Update_Startup_button = tk.Button(window, text="Update and Start", command=lambda: CS2.send_command_to_CS2("!START -U"))
    Update_Startup_button.grid(row=2, column=1, padx=5)

    ShutdownNO_button = tk.Button(window, text="Back", command=main)
    ShutdownNO_button.grid(row=2, column=2, padx=5, sticky="w")

    update_IP_button = tk.Button(window, text="Update IP", command=lambda: update_and_display_ip())
    update_IP_button.grid(row=3, column=1, pady=10)

    result_label = tk.Label(window, textvariable=result_variable)
    result_label.grid(row=4, column=1, pady=5)

    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)
    window.columnconfigure(2, weight=1)

def shutdown():
    for widget in window.winfo_children():
        widget.destroy()

    Confirm_label = tk.Label(window, text="Are You Sure?")
    Confirm_label.grid(row=1, column=0, columnspan=2, pady=10)

    ShutdownYES_button = tk.Button(window, text="Yes", command=lambda: CS2.send_command_to_CS2("!STOP"))
    ShutdownYES_button.grid(row=2, column=0, padx=10, sticky="e")

    ShutdownNO_button = tk.Button(window, text="Back", command=main)
    ShutdownNO_button.grid(row=2, column=1, padx=10, sticky="w")

    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)
    
    pass

def update_and_display_ip():
    # Call the function and update the Tkinter variable
    result_variable.set(CS2.update_IP())
    

    

if __name__ == "__main__":
    login()