from sqlStatements.passwordSqlStatements import createNewPasswordSql, getAllPasswordsSql, getPasswordByIdSql, modifyAPasswordSql, deletePasswordByIdSql
from utils.errorMessages import errorToCreateAPassword, errorToGetAllPasswords, errorToGetPasswordById, errorToModifyAPassword, errorToDeletePasswordById
from Connection import Connection

class Password:
    def __init__(self):
        instaConnection = Connection()
        self.connection = instaConnection.getConnection()
        self.cursor = instaConnection.getCursor()

    def createNewPassword(self, passwordData):
        try:
            self.cursor.execute(createNewPasswordSql, passwordData)
            self.connection.commit()
            return {"success": True}
        except:
            print(errorToCreateAPassword)
            return {"success": False}

    def getAllPasswords(self):
        try:
            self.cursor.execute(getAllPasswordsSql)
            passwordsData = self.cursor.fetchall()
            return {"success": True, "passwordsData": passwordsData}
        except:
            print(errorToGetAllPasswords)
            return {"success": False, "passwordsData": ()}

    def getPasswordById(self, passwordId):
        try:
            self.cursor.execute(getPasswordByIdSql, [passwordId])
            passwordData = self.cursor.fetchall()
            return {"success": True, "passwordData": passwordData}
        except:
            print(errorToGetPasswordById)
            return {"success": False, "passwordData": ()}

    def modifyAPassword(self, passwordData):
        try:
            self.cursor.execute(modifyAPasswordSql, passwordData)
            self.connection.commit()
            return { "success": True }
        except:
            print(errorToModifyAPassword)
            return { "success": False }
    def deletePasswordById(self, passwordId):
        try:
            self.cursor.execute(deletePasswordByIdSql, [passwordId])
            self.connection.commit()
            return {"success": True}
        except:
            print(errorToDeletePasswordById)
            return {"success": False}