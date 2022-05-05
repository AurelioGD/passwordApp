from getpass import getpass
from User import User

user = User()

def drawModifyPassword():
    password = getpass("Enter your pasword: ")
    dataPass = user.checkPassword(1, password)
    if len(dataPass) == 0:
        return { "success": False }
    passwordId = input("Enter the password id to modify: ")
    name = input("Enter the new name: ")
    url = input("Enter the new url: ")
    user_name = input("Enter the new user name: ")
    password = getpass("Enter the new password: ")
    description = input("Enter the new desciption: ")
    return {"success": True, "passwordData":[name, url, user_name, password , description, int(passwordId)]}
