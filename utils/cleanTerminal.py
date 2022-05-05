from os import system, name
#‘posix’ – UNIX
#‘mac’ – Apple
#‘java’ – Máquina virtual de Java
#‘nt’, ‘dos’, ce – Sistemas operativos desarrollados por Microsoft 

COMMANDS_TO_CLEAR_TERMINAL = {
    "posix": "clear",
    "mac": "clear",
    "java": "clear", 
    "nt": "cls", 
    "dos": "cls", 
    "ce": "cls"
}

def cleanTerminal():
    system(COMMANDS_TO_CLEAR_TERMINAL.get(name))

