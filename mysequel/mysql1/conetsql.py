import mysql.connector as connection

# import mysql.connector as conn
mydb = connection.connect(host="localhost", user="root", passwd="wandi_1979")
print(mydb)
# print(cursor.fetchall())
cursor = mydb.cursor()
#cursor.execute("create  database wanjiru")
# cursor.execute("show databases")

s =("create table wanjiru.UNi(emp_id int(10) ,emp_name varchar(80) , emp_mailid varchar (20), emp_salary int(6), emp_attendance int(3))")
q1 = cursor.execute(s)
#q2 = cursor.execute("select * from wanjiru .UNi")
#print(q2)

# put some data in the table made. we create a new filehdjdk
# put some data in the table made. we create a new filehdjdk
# put some data in the table made. we create a new filehdjdk