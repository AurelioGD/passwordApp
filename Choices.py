from urllib import response
from Password import Password
from utils.cleanTerminal import cleanTerminal
from utils.drawAddPassword import drawAddPassword
from utils.drawDeletePassword import drawDeletePassword
from utils.drawMessage import drawMessage
from tabulate import tabulate
from utils.drawModifyPassword import drawModifyPassword

from utils.drawSpecificPassword import drawSpecificPassword
password = Password()
class Choices:
    def addPassword():
        cleanTerminal()
        passwordData = drawAddPassword()
        response = password.createNewPassword(passwordData)
        isSuccess = response.get("success")
        cleanTerminal()
        if(isSuccess): drawMessage("Password was created correctly")
    def displayAllPasswords():
        cleanTerminal()
        passwordsData = password.getAllPasswords().get("passwordsData")
        headers = ['id', "name", "url", "user", "password", "description"]
        table = tabulate(passwordsData, headers, tablefmt="fancy_grid")
        print(table)
    def displayAPassword():
        passwordId = drawSpecificPassword()
        passwordData = password.getPasswordById(passwordId).get("passwordData")[0]
        table = tabulate([[passwordData[0], passwordData[1], passwordData[2], passwordData[3], passwordData[4], passwordData[5]]], tablefmt="fancy_grid")
        print(table)
    def modifyAPassword():
        passwordData = drawModifyPassword()
        if passwordData.get("success"):
            response = password.modifyAPassword(passwordData.get("passwordData"))
            if(response.get("success")):
                drawMessage("The password is changed successfully")
    def deleteAPassword():
        passwordId = drawDeletePassword()
        if(passwordId.get("success")):
            response = password.deletePasswordById(passwordId.get("passwordId"))
            if response.get("success"):
                drawMessage("The password was removed successfully")
    ACTIONS = {
        "1": addPassword,
        "2": displayAllPasswords,
        "3": displayAPassword,
        "4": modifyAPassword,
        "5": deleteAPassword,
        "Incorrect_choice": lambda : print("Option entered is incorrect") 
    }