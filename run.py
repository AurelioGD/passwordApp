from utils.drawMessage import drawMessage
from utils.errorMessages import errorToAuthenticateUser
from utils.cleanTerminal import cleanTerminal
from Connection import Connection
from Authenticate import Authenticate
from optionMenu import optionMenu

db = Connection()
db.createDatabaseStructure()
db.getConnection().close()

def run():
    cleanTerminal()

    while True:
        response = Authenticate()
        cleanTerminal()
        isAuthenticated = response.get("success")
        if(isAuthenticated):
            userName = response.get("userData")[0]
            cleanTerminal()
            optionMenu(userName)
            break;
        else:
            drawMessage(errorToAuthenticateUser)
run()