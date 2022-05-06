from utils.drawRegister import drawRegister
from utils.drawLogin import drawLogin

from User import User

user = User()

def Authenticate():
    existingUser = user.checkUser()
    if len(existingUser) == 0:
        dataNewUser = drawRegister()
        response = user.register(dataNewUser[0], dataNewUser[1], dataNewUser[2])
        if response.get("success"):
            return {"success": True, "userData": dataNewUser}
        else:
            return {"success": False, "userData": ()}
    else:
        password = drawLogin()
        dataUser = user.checkPassword(1, password)
        if len(dataUser) == 0:
            return {"success": False, "userData": ()}
        else:
            return {"success": True, "userData": (dataUser[0][1],dataUser[0][2],dataUser[0][3])}