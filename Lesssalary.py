import sqlite3

conn = sqlite3.connect('Employee.db')

conn.execute('''CREATE TABLE Employee_details
                (ID INT PRIMARY KEY NOT NULL,
                Fname TEXT NOT NULL,
                Lname TEXT NOT NULL,
                salary INT);''')
print("table created successfully")

conn.execute('''insert into Employee_details(ID,Fname,Lname,salary)
 values(1,'Sharath','kumar',7000)''')
conn.execute('''insert into Employee_details(ID,Fname,Lname,salary)
 values(2,'Rithik','B',5000)''')
conn.execute('''insert into Employee_details(ID,Fname,Lname,salary)
 values(3,'Rishi','H',8000)''')
conn.execute('''insert into Employee_details(ID,Fname,Lname,salary)
 values(4,'Krishna','H',6000)''')
print("record is inserted:")

conn.commit()
print("all records")

res=conn.execute('''select * from Employee_details;''')
print(res)
for row in res:
 print(row[0], " ", row[1], " ", row[2], " ", row[3])
print("QUERY")
res=conn.execute('''select * from Employee_details where salary<6000;''')
for row in res:
 print(row[0], " ", row[1], " ", row[2], " ", row[3])
conn.close()