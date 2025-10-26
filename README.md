### linux-terminal-multitools

# Multitools Script

The **Multitools Script** is a simple Python script that emulates a Unix/Linux-like command-line interface (CLI). It allows users to simulate basic terminal commands such as `pwd` and `ls`, while providing a colorful and interactive user interface.

The script uses the `colorama` module to add colors to terminal output, enhancing the user experience with vibrant terminal displays. It also provides additional functionality, such as opening a web browser directly from the terminal to visit a predefined link.

## Main Features:
1. **Unix Terminal Simulation**:
   - The script simulates a terminal with a personalized prompt that displays the username and machine name.
   - It checks whether the user is `root` or not, adapting the prompt accordingly.

2. **Basic Commands**:
   - **`pwd`**: Displays the current working directory.
   - **`ls`**: Lists predefined folders (`Desktop`, `Documents`, `Downloads`, etc.) and a Python file `multitools.py` in the directory.

3. **Running `multitools.py`**:
   - The script can be run using the command `python multitools.py` or `python3 multitools.py` to launch a custom multitasking tool.

4. **Interactive Display**:
   - Upon execution, the script displays colorful text with interactive options, allowing the user to select actions.
   - For example, option 1 opens a browser to visit a GitHub profile link.

5. **Colorful Interface**:
   - The interface is visually enriched using the `colorama` library, which makes the user interaction more engaging and clear.

6. **Interactive Menu**:
   - After executing certain commands, the interactive menu prompts the user to choose an option (such as opening a browser).

## Code Walkthrough:

1. **Initialization**:
   - The script initializes color settings and retrieves user and machine information via the `getpass` and `platform` modules.
   - It creates a customized prompt that displays the username and machine name on which the script is running.

2. **Displaying Information**:
   - Stylized text is displayed during the script's execution, with custom colors for each line of text.
   - It also includes a copyright message and a link to the author's GitHub profile.

3. **Menu Functionality**:
   - The script displays a menu with options (currently, one option to open a browser).
   - After displaying the menu, the script waits for user input. If option 1 is selected, a browser opens with the predefined GitHub link.

4. **Command Handling**:
   - The script recognizes commands like `pwd` and `ls`, executing specific actions for each command (e.g., displaying the working directory or listing files/folders).
   - If the user inputs an unrecognized command, an error message is displayed.

5. **Infinite Loop**:
   - The script runs in an infinite loop (`while True`), allowing the user to input commands continuously without needing to restart the program.
