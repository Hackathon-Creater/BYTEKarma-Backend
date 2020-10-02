import sqlite3
#import json

#conn = sqlite3.connect('database.db')
#print ("Opened database successfully...")
#conn.execute('DROP TABLE PD_TABLE')
#conn.execute('CREATE TABLE PD_TABLE (cif INT, pod FLOAT, gambling FLOAT, amazon FLOAT, shopping FLOAT, food FLOAT, movie FLOAT, cc_bill FLOAT,customer_contacted INT, create_date DATETIME)')
#print ("New table created successfully...")
#conn.close()

conn = sqlite3.connect('database.db')
print ("Opened database successfully...")
#conn.execute('DROP TABLE PD_TABLE')
conn.execute('CREATE TABLE PD_TABLE (cif INT, pod FLOAT, gambling FLOAT, amazon FLOAT, shopping FLOAT, food FLOAT, movie FLOAT, cc_bill FLOAT,customer_contacted INT ,create_date DATETIME )')
print ("New table created successfully...")
conn.close()

#sqlite_select_query = """"

#cursor = conn.cursor()
#
#cursor.execute("select avg(pod), avg(gambling), avg(amazon), avg(shopping), avg(food), avg(movie), avg(cc_bill) from PD_TABLE")
#
#records = cursor.fetchall()


#for row in records:
#    print(type(row))
#    print(row.)

#print(records[0])

conn = sqlite3.connect('database.db')
print ("Opened database successfully...")
#conn.execute('DROP TABLE INFO_TABLE')
conn.execute('CREATE TABLE INFO_TABLE (cif INT, gender VARCHAR(15), name VARCHAR(150), city VARCHAR(25), state VARCHAR(55), country VARCHAR(55), region VARCHAR(10), create_date DATETIME)')
print ("New table created successfully...")
conn.close()

#cursor = conn.cursor()
#
#cursor.execute("select * from info_table")
#
#records = cursor.fetchall()
#
#for row in records:
#    print(row[i++] + " " + row[i++])