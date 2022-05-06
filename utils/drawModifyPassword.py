from getpass import getpass
from User import User
from Password import Password
user = User()
passwordInstance = Password()
def drawModifyPassword():
    password = getpass("Enter your pasword: ")
    dataPass = user.checkPassword(1, password)
    if len(dataPass) == 0:
        return { "successUser": False }
    passwordId = input("Enter the password id to modify: ")
    responsePassword = passwordInstance.getPasswordById(passwordId)
    if(responsePassword.get("success")):
        if len(responsePassword.get("passwordData")) == 0:
            return { "successUser": True, "passwordExist": False }
    else:
        return { "successUser": True, "passwordExist": False }
    name = input("Enter the new name: ")
    url = input("Enter the new url: ")
    user_name = input("Enter the new user name: ")
    password = getpass("Enter the new password: ")
    description = input("Enter the new desciption: ")
    return {"successUser": True, "passwordExist": True,"passwordData":[name, url, user_name, password , description, int(passwordId)]}
