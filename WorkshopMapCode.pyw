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
dropdown_menu = tk.OptionMenu(window, dropdown_var, "Casual", "Arms Race", "Deathmatch", "Survival")
dropdown_menu.pack(pady=5)

def generate_code():
    map_name = textbox1.get()
    map_code = textbox2.get()
    game_mode = dropdown_var.get()
    
    button_code = f'WS_{map_name}{game_mode}_button = tk.Button(window, text="{game_mode} {map_name}", command=lambda: CS2.workshop("{map_name}{game_mode}"))\nWS_{map_name}{game_mode}_button.grid(row=0, column=0)'
    backend_code = f'case "{map_name}{game_mode}":\n    CS2.send_command_to_CS2("game_alias {game_mode.lower()}")\n    CS2.send_command_to_CS2("host_workshop_map {map_code}")'
    
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

validation_label = tk.Label(window, text="Please validate the code and make adjustments to the rows and columns as needed.")
validation_label.pack(pady=10)

window.mainloop()