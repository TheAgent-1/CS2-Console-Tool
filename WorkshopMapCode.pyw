import tkinter as tk

window = tk.Tk()
window.title("Workshop Map Tool")
window.geometry("800x600")

label1 = tk.Label(window, text="Map Name:")
label1.pack(pady=5)
textbox1 = tk.Entry(window, width=50)
textbox1.pack(pady=5)

label2 = tk.Label(window, text="Map Code:")
label2.pack(pady=5)
textbox2 = tk.Entry(window)
textbox2.pack(pady=5)

label3 = tk.Label(window, text="Game Mode:")
label3.pack(pady=5)
dropdown_var = tk.StringVar(window)
dropdown_var.set("Casual")  # default value
dropdown_menu = tk.OptionMenu(window, dropdown_var, "Casual", "Arms Race", "Deathmatch")
dropdown_menu.pack(pady=5)

label4 = tk.Label(window, text="Casual Mode:")
label4.pack(pady=5)
dropdown2_var = tk.StringVar(window)
dropdown2_var.set("Bomb")  # default value
dropdown2_menu = tk.OptionMenu(window, dropdown2_var, "Bomb", "Hostage")
dropdown2_menu.pack(pady=5)

def generate_code():
    map_name = textbox1.get()
    map_code = textbox2.get()
    game_mode = dropdown_var.get()
    casual_mode = dropdown2_var.get()
    
    frame_mapping = {
        "Casual": {"Bomb": "Bomb_frame", "Hostage": "Hostage_frame"},
        "Arms Race": "Armsrace_frame",
        "Deathmatch": "Deathmatch_frame"
    }
    
    frame = frame_mapping.get(game_mode, "window")
    if isinstance(frame, dict):
        frame = frame.get(casual_mode, "window")
    
    display_game_mode = "Arms" if game_mode == "Arms Race" else game_mode
    
    button_code = f'WS_{map_name}{display_game_mode}_button = tk.Button({frame}, text="{display_game_mode} {map_name}", command=lambda: CS2.workshop("{map_name}{display_game_mode}"))\nWS_{map_name}{display_game_mode}_button.pack()'
    backend_code = f'case "{map_name}{display_game_mode}":\n    CS2.send_command_to_CS2("game_alias {game_mode.lower().replace(" ", "")}")\n    CS2.send_command_to_CS2("host_workshop_map {map_code}")'
    
    textbox3.config(state=tk.NORMAL)
    textbox3.delete(1.0, tk.END)
    textbox3.insert(tk.END, button_code)
    textbox3.config(state=tk.DISABLED)
    
    textbox4.config(state=tk.NORMAL)
    textbox4.delete(1.0, tk.END)
    textbox4.insert(tk.END, backend_code)
    textbox4.config(state=tk.DISABLED)

go_button = tk.Button(window, text="Go", command=generate_code)
go_button.pack(pady=10)

label4 = tk.Label(window, text="Button Code:")
label4.pack(pady=5)
textbox3 = tk.Text(window, height=4, width=120, state=tk.DISABLED)
textbox3.pack(pady=5)

label5 = tk.Label(window, text="Backend Code:")
label5.pack(pady=5)
textbox4 = tk.Text(window, height=6, width=120, state=tk.DISABLED)
textbox4.pack(pady=5)

window.mainloop()