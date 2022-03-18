import sqlite3

conn = sqlite3.connect("string.db")

conn.execute('''CREATE table Event1(
                Activity TEXT NOT NULL,
                MONTH TEXT NOT NULL,
                Organizer TEXT NOT NULL
                );''')
conn.execute('''insert into Event1(Activity,MONTH,Organizer)values
                ('Birthday','OCTOBER','XYZ'),
                ('Marriage','AUGUST','ABC'),
                ('Sangeeth','SEPTEMBER','SINGING'),
                ('Proposal','NOVEMBER','ARTS'),
                ('Standup','AUGUST','STUDY');''')
conn.commit()

res=conn.execute('''select * from Event1''')
print("Table of event details")
print("Activity\t MONTH\t Organizer\t ")
for row in res:
 print(row[0],"\t",row[1],"\t",row[2],)
print("\t")
res=conn.execute('''select * from Event1 where Month like '%AUGUST' AND
Organizer='ABC' ;''')
print("WHERE clause to show events :")
print("Activity\t MONTH\t Organizer\t ")
for row in res:
 print(row[0], "\t", row[1], "\t", row[2], )
conn.close()