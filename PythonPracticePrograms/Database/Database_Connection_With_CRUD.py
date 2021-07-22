import sqlite3
class DB_Operations:
    def dbConnection(self):
        con = sqlite3.connect("Test.db")
        self.curs = con.cursor()
        print("Curser created successfully")

    def createTable(self,tbname,tpl):
        self.curs.execute(f'create table {tbname}{tpl}')
        print("Table created....")

    def insertData(self,lst):
        totalRecords = len(lst)
        for i in totalRecords:

obj = DB_Operations()
obj.dbConnection()
obj.createTable('emp',('eid','ename'))