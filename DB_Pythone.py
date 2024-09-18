import mysql.connector as con
db=con.connect(host='localhost',user='root',password='',database='dbdemo')
print("connected successfylly!")

cur=db.cursor()

#  1.  create database

cur.execute("create database DBdemo")
print("Database created...")

cur.execute("use DBdemo")

#  2. table create

cur.execute("create table employee(id int,name varchar(20))")
print("Table created...")

#  3. insert record

query="INSERT INTO employee VALUES(%s,%s)"
list1=[(2,"Dev"),(3,"Ram")]
cur.executemany(query,list1)
db.commit()
print(cur.rowcount," record inserted successfully.")

# 4. update record

query="update employee set name=%s where id=%s"
value=("Ved",2)
cur.execute(query,value)
db.commit()

# 5. Delete records

query="delete from employee where id=%s"
value=(3,)
cur.execute(query,value)
db.commit()

# 6. view records

cur.execute("SELECT * FROM employee")
show=cur.fetchall()
print(show)