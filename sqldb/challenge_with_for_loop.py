#!/usr/bin/python3

import sqlite3
conn = sqlite3.connect('challenge.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE if not exists thursday
 (ID INT PRIMARY KEY     NOT NULL,
 band           TEXT    NOT NULL,
 hometown TEXT          NOT NULL,
 year       int not null) ;''')
print("Table created successfully")


#conn.execute("INSERT INTO thursday (ID,band,hometown,year) VALUES (1, 'The Beatles', 'Liverpool, England', 1960)")
#conn.execute("INSERT INTO thursday (ID,band,hometown,year) VALUES (2, 'Guns and Roses', 'Los Angeles, USA', 1985)")
#conn.execute("INSERT INTO thursday (ID,band,hometown,year) VALUES (3, 'Agnee', 'Pune, India', 2007)")

#conn.commit()
#print("Records created successfully")

x = conn.execute("SELECT id, band, hometown, year from thursday")

for row in x:
    print(row)

conn.close()
