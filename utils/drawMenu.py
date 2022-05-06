def drawMenu():
    print("Select one of the next options: ")
    print("\t1- Add password")
    print("\t2- Display all passwords")
    print("\t3- Display a specific password")
    print("\t4- Modify a password")
    print("\t5- Delete a password")
    print("\t6- Exit")
    choice = input("Enter an option: ")
    if(choice.isnumeric()):
        return int(choice)
    else:
        return choice