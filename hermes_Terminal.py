

import colorama 
colorama.init()
from colorama import Fore, Style, Back
import time
import socket

def typer(message):
    for char in message:
        print(char, end='')
        time.sleep(0.07)
    print('')
    
def clear():
    print('\033[H\033[J', end='')

host_name = socket.gethostname()
a = Fore.GREEN + "v1.0.0b" + Style.RESET_ALL
print(f""" _    _                               
| |  | | {a}                             
| |__| | ___ _ __ _ __ ___   ___  ___ 
|  __  |/ _ \ '__| '_ ` _ \ / _ \/ __|
| |  | |  __/ |  | | | | | |  __/\___
|_|  |_|\___|_|  |_| |_| |_|\___||___/    
                             
Copyright (c) 2023 Shanahan Information and Technology Inc.""")
termLoop = True
while termLoop == True:
    userInput = input(Fore.GREEN + f"{host_name}@hermes" + Style.RESET_ALL + ":" + Fore.BLUE + "~" + Style.RESET_ALL + '$ ')
    if userInput == "ipAdr":
        host_ip = socket.gethostbyname(host_name)
        print(host_ip)
    elif "display" in userInput:
        try:
            start = userInput.index('"') + 1
            end = userInput.rindex('"')
            print(userInput[start:end])
        except:
            pass
    elif "typeOut" in userInput:
        try:
            start = userInput.index('"') + 1
            end = userInput.rindex('"')
            typer(userInput[start:end])
        except:
            pass
    elif userInput == "clear":
        try:
            clear()
        except:
            pass
    elif '+' in userInput:
        try:
            result = eval(userInput)
            print(result)
        except:
            pass
    elif '-' in userInput:
        try:
            result = eval(userInput)
            print(result)
        except:
            pass
    elif '*' in userInput:
        try:
            result = eval(userInput)
            print(result)
        except:
            pass
    elif '/' in userInput:
        try:
            result = eval(userInput)
            print(result)
        except:
            pass
    else:
        print(f"'{userInput}' is not recognized as an internal or external command")