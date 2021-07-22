import mysql.connector as mcn

class DbConnect:
    def __init__(self):
        self.con = ''
        self.cursor = ''

    def createConnection(self):
        try:
            self.con = mcn.connect(host="localhost", database="tq_db", username="root", password="root")
        except Exception as e:
            print("\nCaught Error :- ", e, "\n")
        else:
            print("Connection created successfully.....")

    def createCursor(self):
        try:
            self.cursor = self.con.cursor()
        except Exception as e:
            print("\nCaught Error :- ", e, "\n")
        else:
            print("Cursor created successfully.....")