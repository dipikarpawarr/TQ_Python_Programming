import mysql.connector as mcn
import Database_MySQL.DB_Connect as d

class MySQL_CRUD_Operations:
    def __init__(self):
        self.con = ''
        self.cursor = ''

    def createConnection(self):
        try:
            self.con = mcn.connect(host="localhost",database="tq_db",username="root",password="root")
            self.cursor = self.con.cursor()
        except Exception as e:
            print("\nCaught Error :- ", e,"\n")
        else:
            print("Connection & Cursor created successfully.....")

    def createNewTable(self,tablename,d):
        try:
            MySQL_CRUD_Operations.createConnection()
            tableData = "("
            cnt = 0

            for k,v in d.items():
                if cnt == len(d)-1:
                    tableData += k + " " + v +")"
                else:
                    tableData += k + " " + v + ","
                cnt +=1

            self.cursor.execute(f'create table if not exists {tablename} {tableData}')

        except Exception as e:
            print("\nCaught Error :- ", e,"\n")
            self.con.rollback()
        else:
            self.con.commit()
            print("Table Created Successfully")
        finally:
            self.con.close()
            self.cursor.close()

    def insertManyData(self,tablename,dataTuple):
        strParam=""
        length = len(dataTuple[0])
        if length==0:
            return "error"
        for i in range(length-1):
            strParam += "%s,"
        strParam += "%s"

        try:
            query = "insert into " + tablename + " values("+ strParam +")"
            self.cursor.executemany(query, dataTuple)
        except Exception as e:
            print("Caught Error :- ", e)
            self.con.rollback()
        else:
            self.con.commit()
            print("Multiple records inserted successfully....")
        finally:
            self.con.close()
            self.cursor.close()

    def insertOneRecord(self,tablename,sid,sname):
        try:
            #MySQL_CRUD_Operations.createConnection()
            query = 'insert into ' + tablename + '(sid,sname) values(%s,%s)('
            self.cursor.execute(query,sid,sname + ")")
        except Exception as e:
            print("\nCaught Error :- ", e,"\n")
            #  self.con.rollback()
        else:
            self.con.commit()
            print("Record inserted successfully....")
        finally:
            self.con.close()
            self.cursor.close()

    def updateData(self,sid, sname):
        try:
            #MySQL_CRUD_Operations.createConnection()
            query = 'update stud set sname=%s where sid=%s'
            dataTuple = (sname, sid)
            self.cursor.execute(query, dataTuple)
            self.con.commit()
        except Exception as e:
            print("\nCaught Error :- ", e,"\n")
            self.con.rollback()
        else:
            self.con.commit()
            print("Record updated successfully ....")
        finally:
            self.con.close()
            self.cursor.close()

    def deleteData(self,tablename,sid):
        try:
            #MySQL_CRUD_Operations.createConnection()
            query = f'delete from {tablename} where sid=%s'
            self.cursor.execute(query,tuple(sid))
        except Exception as e:
            print("\nCaught Error :- ", e, "\n")
          #  self.con.rollback()
        else:
            self.con.commit()
            print("Record deleted successfully ....")
        # finally:
        #     self.con.close()
        #     self.cursor.close()




obj = MySQL_CRUD_Operations()
#obj.createConnection()

tablename = "stud"

d = {'sid':"int",'sname':'varchar(10)'}
#obj.createNewTable(tablename,d)

# insData = [(1,'dipika'),(2,'Swapnil'),(3,'Praneet')]
# obj.createConnection()
# obj.insertManyData(tablename,insData)
#
obj.insertOneRecord(tablename,4,'Vineet')
#
# obj.updateData(1, "www")
#
#obj.deleteData(tablename,4)