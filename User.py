import hashlib
from Connection import Connection
from utils.errorMessages import errorToRegisterUser, errorToCheckPassword, errorToCheckUser
from sqlStatements.userSqlStatements import getAllUsersSql, registerAUserSql, checkPasswordSql

class User:
    def __init__(self):
        instaConnection = Connection()
        self.connection = instaConnection.getConnection()
        self.cursor = instaConnection.getCursor()
    def checkUser(self):
        try:
            self.cursor.execute(getAllUsersSql)
            userData = self.cursor.fetchall()
            self.connection.commit()
            return userData
        except:
            print(errorToCheckUser)
    def checkPassword(self, userId, password):
        try:
            encryptedPassword = hashlib.sha256(password.encode('utf-8')).hexdigest()
            self.cursor.execute(checkPasswordSql, [userId, encryptedPassword])
            data = self.cursor.fetchall()
            return data 
        except:
            print(errorToCheckPassword)
    def register(self, name, last_name, password):
        try:
            encryptedPassword = hashlib.sha256(password.encode('utf-8')).hexdigest()
            newUser = (name, last_name, encryptedPassword)
            self.cursor.execute(registerAUserSql, newUser)
            self.connection.commit()
            return { "success": True }
        except:
            print(errorToRegisterUser)
            return { "success": False }


