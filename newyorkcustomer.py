import sqlite3

conn = sqlite3.connect('Customer.db')

conn.execute('''CREATE TABLE Customerdetails
                (ID INT PRIMARY KEY NOT NULL,
                NAME TEXT NOT NULL,
                CITY TEXT NOT NULL,
                SALES_ID TEXT NOT NULL,
                GRADE INT);''')
print("table created successfully")

conn.execute('''insert into Customerdetails(ID,NAME,CITY,SALES_ID,GRADE)
 values(1,'John','New YORK','4',10)''')
conn.execute('''insert into Customerdetails(ID,NAME,CITY,SALES_ID,GRADE)
 values(2,'Shiva','Delhi','7',20)''')
conn.execute('''insert into Customerdetails(ID,NAME,CITY,SALES_ID,GRADE)
 values(3,'Abdul','New YORK','8',300)''')
print("record is inserted:")

conn.commit()

print("all records")
res=conn.execute('''select * from Customerdetails;''')

print(res)
for row in res:
 print(row[0], " ", row[1], " ", row[2], " ", row[3]," ",row[4])
print("QUERY")
res=conn.execute('''select * from Customerdetails where city like '%New YORK' 
AND GRADE>100;''')
for row in res:
 print(row[0], " ", row[1], " ", row[2], " ", row[3]," ",row[4])
conn.close()
