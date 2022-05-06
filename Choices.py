from utils.errorMessages import errorNotIsANumber, errorDatabase, errorToAuthenticateUser, errorNotExistPassword, errorNotExistPasswordToModify, errorNotExistPasswordToDelete,errorOptionEnteredIncorrect
from utils.isNotNumber import isNotNumber
from utils.cleanTerminal import cleanTerminal
from utils.drawAddPassword import drawAddPassword
from utils.drawDeletePassword import drawDeletePassword
from utils.drawMessage import drawMessage
from utils.drawModifyPassword import drawModifyPassword
from utils.drawSpecificPassword import drawSpecificPassword
from Password import Password
from tabulate import tabulate

password = Password()

headers = ['id', "name", "url", "user", "password", "description"]
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
        
        table = tabulate(passwordsData, headers, tablefmt="fancy_grid")
        print(table)
    def displayAPassword():
        passwordId = drawSpecificPassword()
        if isNotNumber(passwordId): 
            cleanTerminal()
            drawMessage(errorNotIsANumber)
            return
        cleanTerminal()
        response = password.getPasswordById(passwordId)
        if response.get("success"):
            responsePasswordData = response.get("passwordData")
            if len(responsePasswordData) > 0:
                passwordData = responsePasswordData[0]
                table = tabulate([[passwordData[0], passwordData[1], passwordData[2], passwordData[3], passwordData[4], passwordData[5]]], headers, tablefmt="fancy_grid")
                print(table)
            else:
                cleanTerminal()
                drawMessage(errorNotExistPassword)
        else:
            cleanTerminal()
            drawMessage(errorDatabase)
        
    def modifyAPassword():
        cleanTerminal()
        passwordData = drawModifyPassword()
        if passwordData.get("successUser"):
            if passwordData.get("passwordExist"):
                response = password.modifyAPassword(passwordData.get("passwordData"))
                if(response.get("success")):
                    cleanTerminal()
                    drawMessage("The password is changed successfully")
                else:
                    cleanTerminal()
                    drawMessage(errorDatabase)
            else:
                cleanTerminal()
                drawMessage(errorNotExistPasswordToModify)
        else:
            cleanTerminal()
            drawMessage(errorToAuthenticateUser)
    def deleteAPassword():
        cleanTerminal()
        passwordData = drawDeletePassword()
        if(passwordData.get("successUser")):
            if passwordData.get("passwordExist"):
                response = password.deletePasswordById(passwordData.get("passwordId"))
                if response.get("success"):
                    cleanTerminal()
                    drawMessage("The password was removed successfully")
                else:
                    cleanTerminal()
                    drawMessage(errorDatabase)
            else:
                cleanTerminal()
                drawMessage(errorNotExistPasswordToDelete)
        else:
            cleanTerminal()
            drawMessage(errorToAuthenticateUser)
    ACTIONS = {
        "1": addPassword,
        "2": displayAllPasswords,
        "3": displayAPassword,
        "4": modifyAPassword,
        "5": deleteAPassword,
        "Incorrect_choice": lambda : drawMessage(errorOptionEnteredIncorrect)
    }