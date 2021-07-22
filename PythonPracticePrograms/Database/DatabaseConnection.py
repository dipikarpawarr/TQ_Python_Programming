import sqlite3

con = sqlite3.connect('Test.db')
print("connect successfully")
curs = con.cursor()
print("cursor is created")
#curs.execute("create table stud(sid,sname,mobile)")
#print("Table created successfully")
#curs.execute("insert into stud values (1,'Dipika',8385789432)")
#print("data inserted")
#studData = [(1,'Dipika',8385789432),(2,'Praneet',88476372882),(3,'Swapnil',8765789988)]
#curs.executemany("insert into stud values(?,?,?)",studData)
print("data inseted")
#curs.execute("delete from stud where")
curs.execute("update stud set mobile=:mob where sid=:sid",{"mob":99226622439,"sid":3})
curs.execute("delete from stud where sid=:sid",{"sid":3})
curs.execute("select * from stud")
records = curs.fetchall()
for row in records:
    print(row)
print("values updated")
con.commit()
con.close()
print("---end----")