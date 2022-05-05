from getpass import getpass
from User import User

user = User()
def drawDeletePassword():
    password = getpass("Enter your pasword: ")
    dataPass = user.checkPassword(1, password)
    if len(dataPass) == 0:
        return { "success": False }
    passwordId = input("Enter the password id to delete: ")
    return {"success": True, "passwordId": passwordId}