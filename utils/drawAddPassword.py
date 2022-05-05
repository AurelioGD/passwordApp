from getpass import getpass

def drawAddPassword():
    name = input("Enter a name: ")
    url = input("Enter a url: ")
    user_name = input("Enter a user name: ")
    password = getpass("Enter the password: ")
    description = input("Enter a description: ")
    return (name, url, user_name, password, description)