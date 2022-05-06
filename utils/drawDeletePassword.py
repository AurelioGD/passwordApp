from getpass import getpass
from pickle import TRUE
from User import User
from Password import Password
user = User()
passwordInstance = Password()
def drawDeletePassword():
    password = getpass("Enter your pasword: ")
    dataPass = user.checkPassword(1, password)
    if len(dataPass) == 0:
        return { "successUser": False }
    passwordId = input("Enter the password id to delete: ")
    responsePassword = passwordInstance.getPasswordById(passwordId)
    if(responsePassword.get("success")):
        if len(responsePassword.get("passwordData")) == 0:
            return { "successUser": True, "passwordExist": False }
    else:
        return { "successUser": True, "passwordExist": False }
    return {"successUser": True, "passwordExist": True, "passwordId": passwordId}