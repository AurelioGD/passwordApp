class Choices:
    def addPassword():
        print("adding a pasword")
    def displayAllPasswords():
        print("displaying all passwords")
    def displayAPassword():
        print("displaying a password")
    def modifyAPassword():
        print("modifiying a password")
    def deleteAPassword():
        print("deleting a password")
    ACTIONS = {
        "1": addPassword,
        "2": displayAllPasswords,
        "3": displayAPassword,
        "4": modifyAPassword,
        "5": deleteAPassword,
        "Incorrect_choice": lambda : print("Option entered is incorrect") 
    }