import mysql.connector as connection

# import mysql.connector as conn
db = connection.connect(host="localhost", user="root", passwd="wandi_1979")
cursor = db.cursor()
# print(db)
# cursor.execute("create database mike")
# print(cursor.fetchall())
# cursor.execute("create database marks")

k=("create table marks.students(name varchar(20),subjects varchar(10),year int(6), email_id varchar(15), school varchar(20))")
# k1 = cursor.execute(k)
# k2 = cursor.execute("select * from marks.students")

# print(k2)

#cursor.execute("insert into marks.students values('kamau','maths' , 1912, 'dfg@hm.ai','kericho')")
#db.commit()
#cursor.execute("select * from marks.students")
#for i in cursor.fetchall():
 #   print(i)
cursor.execute("select * from marks.students where school like '%n%'")
for i in cursor.fetchall():
    print(i)
