# Workshop Map Tool GUI Application

The program creates a GUI application using the `tkinter` library to generate code snippets for a Counter-Strike 2 (CS2) console tool. Here's a breakdown of the functionality:

## GUI Elements
- **Map Name Textbox**: Allows the user to input the name of the map.
- **Map Code Textbox**: Allows the user to input the map code.
- **Game Mode Dropdown Menu**: Allows the user to select a game mode from the options: Casual, Arms Race, Deathmatch, and Survival.
- **Go Button**: When clicked, it generates the frontend and backend code snippets based on the user's input.
- **Button Code Textbox**: Displays the generated frontend code for creating a button in the CS2 tool.
- **Backend Code Textbox**: Displays the generated backend code for handling the map in the CS2 tool.
- **Validation Label**: Instructs the user to validate the generated code and make any necessary adjustments.

## Code Generation
- **Frontend Code**: Generates a `tk.Button` widget creation code with a command to call the `CS2.workshop` method.
- **Backend Code**: Generates a `case` statement for the `CS2.workshop` method to handle the map with the specified game mode and map code.

## Example
For a map named "Test" with a game mode of "Casual" and a map code of "111":
- **Button Code**:
  ```python
  WS_TestCasual_button = tk.Button(window, text="Casual Test", command=lambda: CS2.workshop("TestCasual"))
  WS_TestCasual_button.grid(row=0, column=0)
  ```
- **Backend Code**:
  ```python
  case "TestCasual":
      CS2.send_command_to_CS2("game_alias casual")
      CS2.send_command_to_CS2("host_workshop_map 111")
  ```

## Usage
1. Run the script to open the GUI.
2. Enter the map name, map code, and select the game mode.
3. Click the "Go" button to generate the code snippets.
4. Copy the generated code from the textboxes and use it in your CS2 tool.
5. Validate the code and make any necessary adjustments as instructed by the validation label.