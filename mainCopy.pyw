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
    'Jonno': 'Jonno13'
    }

    if username in users and users[username] == password:
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
        CS2.start_flask1(username)
        main()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


def main():
    
    window.title("CS2 GUI")
    window.geometry("620x600") # Add this line to set the window size

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
    #casual - column=0
    #arms - column=1
    #death- column=3
    #1PM - column=4

    for widget in window.winfo_children():
        widget.destroy()

    Back_button = tk.Button(window, text="Back", command=main)
    Back_button.grid(row=0, column=2)


    Casual_label = tk.Label(window, text="Casual", bg="lightblue", font=("Arial", 12, "bold"))
    Casual_label.grid(row=1, column=0)

    Armsrace_label = tk.Label(window, text="Armsrace", bg="lightblue", font=("Arial", 12, "bold"))
    Armsrace_label.grid(row=1, column=1)

    Deathmatch_label = tk.Label(window, text="Deathmatch", bg="lightblue", font=("Arial", 12, "bold"))
    Deathmatch_label.grid(row=1, column=3)

    OnePerMatch_label = tk.Label(window, text="One Per Match", bg="lightblue", font=("Arial", 12, "bold"))
    OnePerMatch_label.grid(row=1, column=4)

    #CASUAL
    WS_rush_button = tk.Button(window, text="Hostage Rush", command=lambda: CS2.workshop("rush"))
    WS_rush_button.grid(row=2, column=0)

    WS_foroglio_button = tk.Button(window, text="Casual Foroglio", command=lambda: CS2.workshop("foroglio"))
    WS_foroglio_button.grid(row=3, column=0)

    WS_assembly_button = tk.Button(window, text="Casual Assembly", command=lambda: CS2.workshop("assembly"))
    WS_assembly_button.grid(row=4, column=0)

    WS_safehouse_button = tk.Button(window, text="Hostage Safehouse", command=lambda: CS2.workshop("safehouse"))
    WS_safehouse_button.grid(row=5, column=0)

    #WS_minimirage_button = tk.Button(window, text="Minimirage", command=lambda: CS2.workshop("minimirage"))
    #WS_minimirage_button.pack()

    WS_minecraft_button = tk.Button(window, text="Hostage Minecraft", command=lambda: CS2.workshop("minecraft"))
    WS_minecraft_button.grid(row=6, column=0)

    #WS_rustdeath_button = tk.Button(window, text="Rust Deathmatch", command=lambda: CS2.workshop("rustdeath"))
    #WS_rustdeath_button.pack()

    WS_blackgold_button = tk.Button(window, text="Casual Black Gold", command=lambda: CS2.workshop("blackgold"))
    WS_blackgold_button.grid(row=7, column=0)

    WS_lake_button = tk.Button(window, text="Bomb Lake", command=lambda: CS2.workshop("lake"))
    WS_lake_button.grid(row=8, column=0)

    #WS_2towers_button = tk.Button(window, text="Two Towers", command=lambda: CS2.workshop("2towers"))
    #WS_2towers_button.pack()

    #WS_nuketown_button = tk.Button(window, text="Nuketown", command=lambda: CS2.workshop("nuketown"))
    #WS_nuketown_button.pack()

    WS_dam_button = tk.Button(window, text="Hostage Dam", command=lambda: CS2.workshop("dam"))
    WS_dam_button.grid(row=9, column=0)

    WS_bank_button = tk.Button(window, text="Bomb Bank", command=lambda: CS2.workshop("bank"))
    WS_bank_button.grid(row=10, column=0)

    WS_bikinibottom_button = tk.Button(window, text="Bomb BikiniBottom", command=lambda: CS2.workshop("bikinibottom"))
    WS_bikinibottom_button.grid(row=11, column=0)

    WS_plane_button = tk.Button(window, text="Bomb Plane", command=lambda: CS2.workshop("plane"))
    WS_plane_button.grid(row=12, column=0)

    WS_stmarc_button = tk.Button(window, text="Bomb StMarc", command=lambda: CS2.workshop("stmarc"))
    WS_stmarc_button.grid(row=13, column=0)

    WS_assault_button = tk.Button(window, text="Hostage Assault", command=lambda: CS2.workshop("assault"))
    WS_assault_button.grid(row=14, column=0)

    WS_sugarcane_button = tk.Button(window, text="Bomb SugarCane", command=lambda: CS2.workshop("sugarcane"))
    WS_sugarcane_button.grid(row=15, column=0)

    #WS_chickens_button = tk.Button(window, text="Bomb Chickens", command=lambda: CS2.workshop("chickens"))
    #WS_chickens_button.grid(row=16, column=0)

    WS_rainbow6_button = tk.Button(window, text="Hostage Rainbow6", command=lambda: CS2.workshop("rainbow6"))
    WS_rainbow6_button.grid(row=17, column=0)

    WS_militia_button = tk.Button(window, text="Hostage Militia", command=lambda: CS2.workshop("militia"))
    WS_militia_button.grid(row=18, column=0)

    WS_astra_button = tk.Button(window, text="Bomb Astra", command=lambda: CS2.workshop("astra"))
    WS_astra_button.grid(row=19, column=0)

    WS_glass_button = tk.Button(window, text="Casual Glass", command=lambda: CS2.workshop("glass"))
    WS_glass_button.grid(row=20, column=0)

    WS_maginot_button = tk.Button(window, text="Bomb Maginot", command=lambda: CS2.workshop("maginot"))
    WS_maginot_button.grid(row=21, column=0)
    
    WS_palais_button = tk.Button(window, text="Bomb Palais", command=lambda: CS2.workshop("palais"))
    WS_palais_button.grid(row=22, column=0)

    WS_omahabeach_button = tk.Button(window, text="Bomb OmhaBeach", command=lambda: CS2.workshop("omahabeach"))
    WS_omahabeach_button.grid(row=23, column=0)
    

    #ARMSRACE
    WS_lunacy_button = tk.Button(window, text="Arms Lunacy", command=lambda: CS2.workshop("lunacy"))
    WS_lunacy_button.grid(row=2, column=1)

    #WS_planearms_button = tk.Button(window, text="Plane Armsrace", command=lambda: CS2.workshop("planearms"))
    #WS_planearms_button.pack()

    WS_monastery_button = tk.Button(window, text="Arms Monastery", command=lambda: CS2.workshop("monastery"))
    WS_monastery_button.grid(row=3, column=1)

    WS_stmarcarms_button = tk.Button(window, text="Arms StMarc", command=lambda: CS2.workshop("stmarcarms"))
    WS_stmarcarms_button.grid(row=4, column=1)

    
    WS_stairsarms_button = tk.Button(window, text="Arms Stairs", command=lambda: CS2.workshop("stairsarms"))
    WS_stairsarms_button.grid(row=5, column=1)

    WS_churchesarms_button = tk.Button(window, text="Arms Churches", command=lambda: CS2.workshop("churchesarms"))
    WS_churchesarms_button.grid(row=6, column=1)

    WS_poolday_button = tk.Button(window, text="Arms PoolDay", command=lambda: CS2.workshop("pooldayarms"))
    WS_poolday_button.grid(row=7, column=1)


    #Deathmatch

    WS_omahabeachdeath_button = tk.Button(window, text="Deathmatch OmhaBeach", command=lambda: CS2.workshop("omahabeachdeath"))
    WS_omahabeachdeath_button.grid(row=2, column=3)
    
    WS_astradeath_button = tk.Button(window, text="Deathmatch Astra", command=lambda: CS2.workshop("astradeath"))
    WS_astradeath_button.grid(row=3, column=3)

    WS_halodeath_button = tk.Button(window, text="Deathmatch Halo", command=lambda: CS2.workshop("halodeath"))
    WS_halodeath_button.grid(row=4, column=3)

    WS_breadwindow_button = tk.Button(window, text="Deathmatch Breadwindow", command=lambda: CS2.workshop("breadwindowarms"))
    WS_breadwindow_button.grid(row=5, column=3)

    #1PM
    WS_blackgold1pm_button = tk.Button(window, text="Black Gold 1PM", command=lambda: CS2.workshop("blackgold1pm"))
    WS_blackgold1pm_button.grid(row=2, column=4)
    
    WS_train_button = tk.Button(window, text="Bomb Train", command=lambda: CS2.workshop("train"))
    WS_train_button.grid(row=3, column=4)

    #WS_turbulence_button = tk.Button(window, text="Flying Scotsman Turbulence", command=lambda: CS2.workshop("turbulence"))
    #WS_turbulence_button.grid(row=4, column=4)

    #WS_invasion_button = tk.Button(window, text="Arms Invasion", command=lambda: CS2.workshop("invasionarms"))
    #WS_invasion_button.grid(row=5, column=4)

    WS_attic_button = tk.Button(window, text="Bomb Attic", command=lambda: CS2.workshop("attic"))
    WS_attic_button.grid(row=4, column=4)
   
    WS_hijack_button = tk.Button(window, text="Hostage HiJack", command=lambda: CS2.workshop("hijack"))
    WS_hijack_button.grid(row=5, column=4)

    #WS_mirage45_button = tk.Button(window, text="Mirage 45", command=lambda: CS2.workshop("mirage45"))
    #WS_mirage45_button.grid(row=7, column=4)

    WS_themetro_button = tk.Button(window, text="Bomb The Metro", command=lambda: CS2.workshop("themetro"))
    WS_themetro_button.grid(row=6, column=4)

    WS_cache_button = tk.Button(window, text="Bomb Cache", command=lambda: CS2.workshop("cache"))
    WS_cache_button.grid(row=7, column=4)

    WS_inca_button = tk.Button(window, text="Bomb Inca", command=lambda: CS2.workshop("inca"))
    WS_inca_button.grid(row=8, column=4)
    
    WS_sparity_button = tk.Button(window, text="Bomb Sparity", command=lambda: CS2.workshop("sparity"))
    WS_sparity_button.grid(row=9, column=4)

    WS_futsal_button = tk.Button(window, text="Football Futsal", command=lambda: CS2.workshop("futsal"))
    WS_futsal_button.grid(row=10, column=4)

    WS_basalt_button = tk.Button(window, text="Bomb Basalt", command=lambda: CS2.workshop("basalt"))
    WS_basalt_button.grid(row=11, column=4)

    WS_zoo_button = tk.Button(window, text="Bomb Zoo", command=lambda: CS2.workshop("zoo"))
    WS_zoo_button.grid(row=12, column=4)

    WS_eternal_button = tk.Button(window, text="Deathmatch Eternal", command=lambda: CS2.workshop("eternal"))
    WS_eternal_button.grid(row=13, column=4)

    WS_mansion_button = tk.Button(window, text="Deathmatch Mansion", command=lambda: CS2.workshop("mansion"))
    WS_mansion_button.grid(row=14, column=4)
    
    WS_aireality_button = tk.Button(window, text="Deathmatch AIReality", command=lambda: CS2.workshop("aireality"))
    WS_aireality_button.grid(row=15, column=4)

    WS_speedball_button = tk.Button(window, text="Arms Speedball", command=lambda: CS2.workshop("speedball"))
    WS_speedball_button.grid(row=16, column=4)

    WS_tuscan_button = tk.Button(window, text="Bomb Tuscan", command=lambda: CS2.workshop("tuscan"))
    WS_tuscan_button.grid(row=17, column=4)

    WS_rainfall_button = tk.Button(window, text="Bomb Rainfall", command=lambda: CS2.workshop("rainfall"))
    WS_rainfall_button.grid(row=18, column=4)

    WS_climb_button = tk.Button(window, text="Hostage Climb", command=lambda: CS2.workshop("climb"))
    WS_climb_button.grid(row=19, column=4)

    WS_lighthousebomb_button = tk.Button(window, text="Bomb Lighthouse", command=lambda: CS2.workshop("lighthousebomb"))
    WS_lighthousebomb_button.grid(row=20, column=4)

    WS_lighthouse_button = tk.Button(window, text="Deathmatch Lighthouse", command=lambda: CS2.workshop("lighthouse"))
    WS_lighthouse_button.grid(row=21, column=4)

    WS_agency_button = tk.Button(window, text="Hostage Agency", command=lambda: CS2.workshop("agency"))
    WS_agency_button.grid(row=22, column=4)

    WS_paris2024_button = tk.Button(window, text="Hostage Paris2024", command=lambda: CS2.workshop("paris2024"))
    WS_paris2024_button.grid(row=23, column=4)

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