from utils.drawMessage import drawMessage
from utils.errorMessages import errorToAuthenticateUser
from utils.cleanTerminal import cleanTerminal
from Connection import Connection
from AuthenticateUser import AuthenticateUser
from optionMenu import optionMenu

db = Connection()
db.createDatabaseStructure()
db.getConnection().close()

def run():
    cleanTerminal()

    while True:
        response = AuthenticateUser()
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