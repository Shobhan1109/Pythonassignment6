import sqlite3

conn = sqlite3.connect('Customer.db')

conn.execute('''CREATE TABLE Event_details
                (ID INT PRIMARY KEY NOT NULL,
                EVENT NAME TEXT NOT NULL,
                EVENT_MONTH TEXT NOT NULL,
                CITY TEXT NOT NULL);''')

print("table created successfully")

conn.execute('''insert into Event_details(ID,EVENT,EVENT_MONTH,CITY)
 values(1,'Birthday','April','Bangalore')''')
conn.execute('''insert into Event_details(ID,EVENT,EVENT_MONTH,CITY)
 values(2,'Marriage','August','Bangalore')''')
conn.execute('''insert into Event_details(ID,EVENT,EVENT_MONTH,CITY)
 values(3,'Engagement','September','Bangalore')''')
conn.execute('''insert into Event_details(ID,EVENT,EVENT_MONTH,CITY)
 values(4,'Proposal','August','Bangalore')''')

print("record is inserted:")

conn.commit()
print("all records")

res=conn.execute('''select * from Event_details;''')
print(res)
for row in res:
 print(row[0], " ", row[1], " ", row[2], " ", row[3])
print("QUERY")

res=conn.execute('''select * from Event_details where event_month like '%August';''')
for row in res:
 print(row[0], " ", row[1], " ", row[2], " ", row[3])
conn.close()