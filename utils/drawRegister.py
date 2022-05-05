from getpass import getpass
def drawRegister():
    print("Welcome, enter your information.")
    name = input("Name: ")
    last_name = input("Last name: ")
    password = getpass("Password: ")
    return (name, last_name, password)