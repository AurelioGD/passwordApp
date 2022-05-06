from utils.drawMenu import drawMenu
from utils.cleanTerminal import cleanTerminal
from utils.drawMessage import drawMessage
from utils.errorMessages import errorNotIsANumber
from utils.isNotNumber import isNotNumber
from Choices import Choices

choices = Choices()

def optionMenu(userName):
    drawMessage(f"Welcome {userName}")
    
    while True:
        choice = drawMenu()
        if isNotNumber(choice): 
            cleanTerminal()
            drawMessage(errorNotIsANumber)
            continue
        if choice == 6: break;
        if choice <= 0 or choice > 6: choice = "Incorrect_choice"

        cleanTerminal()
        
        choices.ACTIONS[str(choice)]()