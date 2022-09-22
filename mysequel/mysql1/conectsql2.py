import mysql.connector as connection

# import mysql.connector as conn
mydb = connection.connect(host="localhost", user="root", passwd="wandi_1979")
cursor = mydb.cursor()
cursor.execute("insert into wanjiru.UNi values(1001, 'asken res' ,'kui@ghn.ai', 100, 30)")
mydb.commit()
cursor.execute("select * from wanjiru.UNi")
for i in cursor.fetchall():
    print(i)
# select a column
cursor.execute("select emp_id ,emp_mailid from wanjiru.UNi")
for i in cursor.fetchall():
    print(i)

# create a list from the above

l = []
cursor.execute("select emp_id ,emp_mailid from wanjiru.UNi")
for i in cursor.fetchall():
    l.append(i)
print(l)
print(type(l[0]))

cursor.execute("create  database marks")

cursor.execute("insert into marks.students values('name','subjects','year', 'email_id', 'school')")
mydb.commit()
