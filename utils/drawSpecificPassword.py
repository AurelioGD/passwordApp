def drawSpecificPassword():
    passwordId = input("Enter the password id: ")
    if(passwordId.isnumeric()):
        return int(passwordId)
    else:
        return passwordId