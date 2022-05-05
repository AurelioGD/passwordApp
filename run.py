from Connection import Connection
from utils.drawMessage import drawMessage
from utils.errorMessages import errorToAuthenticateUser
from authenticateUser import authenticateUser
from optionMenu import optionMenu
from utils.cleanTerminal import cleanTerminal

db = Connection()
db.createDatabaseStructure()
db.getConnection().close()

def run():
    cleanTerminal()

    response = authenticateUser()
    
    cleanTerminal()
    isAuthenticated = response.get("success")
    if(isAuthenticated):
        userName = response.get("userData")[0]
        cleanTerminal()
        optionMenu(userName)
    else:
        drawMessage(errorToAuthenticateUser)
run()