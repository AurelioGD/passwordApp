from Connection import Connection
from sqlStatements.passwordSqlStatements import createNewPasswordSql, getAllPasswordsSql, getPasswordByIdSql
from utils.errorMessages import errorToCreateAPassword, errorToGetAllPasswords, errorToGetPasswordById

class Password:
    def __init__(self):
        instaConnection = Connection()
        self.connection = instaConnection.getConnection()
        self.cursor = instaConnection.getCursor()
    def createNewPassword(self, passwordData):
        try:
            self.cursor.execute(createNewPasswordSql, passwordData)
            self.connection.commit()
            return { "success": True }
        except:
            print(errorToCreateAPassword)
            return { "success": False }
    def getAllPasswords(self):
        try:
            self.cursor.execute(getAllPasswordsSql)
            passwordsData = self.cursor.fetchall()
            return { "success": True, "passwordsData": passwordsData }
        except:
            print(errorToGetAllPasswords)
            return { "success": False, "passwordsData": () }
    def getPasswordById(self, passwordId):
        try:
            self.cursor.execute(getPasswordByIdSql, [passwordId])
            passwordData = self.cursor.fetchall()
            return { "success": True, "passwordData": passwordData }
        except:
            print(errorToGetPasswordById)
            return { "success": False, "passwordData": () }


