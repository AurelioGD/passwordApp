import sqlite3
from sqlite3 import Error
from utils.errorMessages import errorDatabase
from sqlStatements.databaseSqlStatements import createTableUserSql, createTablePasswordSql

class Connection:
    def __init__(self):
        try: 
            self.connection = sqlite3.connect("database.db")
            self.cursor = self.connection.cursor()
        except Error:
            print(errorDatabase)
    def __commitConnection(self):
        self.connection.commit()
    def getConnection(self):
        return self.connection
    def getCursor(self):
        return self.cursor
    def createDatabaseStructure(self):
        self.cursor.execute(createTableUserSql)
        self.cursor.execute(createTablePasswordSql)
        self.__commitConnection()