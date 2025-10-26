# Copyright (c) 2025 Shell Lab
# This script is licensed under the MIT License

from colorama import Fore, init
import getpass
import platform
import webbrowser

init()

user = getpass.getuser()
machine = platform.node()

Fore.LIGHTRED = '\033[38;5;203m'
Fore.LIGHTBLUE = '\033[38;5;69m'
WHITE = Fore.WHITE

prompt_symbol = "#" if user.lower() == "root" else "$"
prompt = f"{user}@{machine}:~{prompt_symbol}"
PASSLINUX = Fore.LIGHTRED + prompt + Fore.RESET

folders = ["Desktop", "Documents", "Downloads", "Music", "Pictures", "Public", "Templates", "Videos"]
pythononls = "multitools.py"

def codepythonmultitool():
    text = r'''  
              .__   __  .__  __                .__       
  _____  __ __|  |_/  |_|__|/  |_  ____   ____ |  |       
 /     \|  |  \  |\   __\  \   __\/  _ \ /  _ \|  |        
|  Y Y  \  |  /  |_|  | |  ||  | (  <_> |  <_> )  |__   
|__|_|  /____/|____/__| |__||__|  \____/ \____/|____/          
      \/                                                      
                                          by github.com/shelllab  
      '''
    colors = [Fore.RED, Fore.WHITE, Fore.BLUE]
    lines = text.split("\n")
    for i, line in enumerate(lines):
        color = colors[i % len(colors)]  
        print(color + line)
####

def display_menu():
    inptext2choose = '''
                         Choose options:
                         
                1 - Open Browser
    ''' 
    for char in inptext2choose:
        print(Fore.LIGHTCYAN_EX + char, end="")
    print()

def open_browser():
    webbrowser.open("https://github.com/shelllab?tab=follow")

def multitools_code():
    codepythonmultitool()
    display_menu()
    inptext2choose = input(PASSLINUX + " ")
    if inptext2choose == '1':
        open_browser()
    else:
        print("Option invalide. Essayez encore.")

while True:
    INPUTPASSLINUX = input(PASSLINUX + " ")

    if INPUTPASSLINUX == 'pwd':
        print(f"/home/{user}")
        
    elif INPUTPASSLINUX == 'ls':
        line = ""
        for folder in folders:
            line += f"{Fore.LIGHTBLUE}{folder}  "
        line += f"{WHITE}{pythononls}  "
        print(line)
        
    elif INPUTPASSLINUX == 'python3 multitools.py':
        multitools_code()
        
    elif INPUTPASSLINUX == 'python multitools.py':
        multitools_code()
    
    else:
        print(f"{INPUTPASSLINUX}: command not found")
