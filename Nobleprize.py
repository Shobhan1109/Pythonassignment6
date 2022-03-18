import sqlite3

conn = sqlite3.connect('NobelPrizer12.db')

conn.execute('''CREATE TABLE NobelPrizer12
                (ID INT PRIMARY KEY NOT NULL,
                NAME TEXT NOT NULL,
                AWARDS TEXT NOT NULL,
                TOPIC TEXT NOT NULL,
                YEAR INT);''')
print("table created successfully")

conn.execute('''insert into NobelPrizer12(ID,NAME,AWARDS,TOPIC,YEAR)
 values(1,'Rishi','Nobelprize','Literature',1971)''')
conn.execute('''insert into NobelPrizer12(ID,NAME,AWARDS,TOPIC,YEAR)
values(2,'Shruthi','BarathRatna','Socialservice',1980)''')
conn.execute('''insert into NobelPrizer12(ID,NAME,AWARDS,TOPIC,YEAR)
 values(3,'Shiva','Nobelprize','Acting',1971)''')
conn.execute('''insert into NobelPrizer12(ID,NAME,AWARDS,TOPIC,YEAR)
 values(4,'Harsha','Padmashri','Sports',2010)''')
print("record is inserted:")

conn.commit()

print("all records")
res = conn.execute('''select * from NobelPrizer12;''')

print(res)
for row in res:
    print(row[0], " ", row[1], " ", row[2], " ", row[3], " ", row[4])
print("QUERY")
res = conn.execute('''select NAME from NobelPrizer12 WHERE AWARDS like 
'%Nobelprize' AND TOPIC like '%Literature' And YEAR='1971';''')
for row in res:
    print(row[0])
conn.close()