from utils.drawMenu import drawMenu
from utils.cleanTerminal import cleanTerminal
from Choices import Choices
from utils.drawMessage import drawMessage
choices = Choices()

def optionMenu(userName):
    drawMessage(f"Welcome {userName}")
    
    while True:
        choice = drawMenu()
        
        if choice == 6: break;
        if choice <= 0 or choice > 6: choice = "Incorrect_choice"

        cleanTerminal()
        
        choices.ACTIONS[str(choice)]()