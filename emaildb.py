__author__ = 'kwoshvick'

import sqlite3

conn = sqlite3.connect('./databases/emaildb')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
create table Counts ( email TEXT, count INTEGER )''')

fname = input('Enter file name: ')
if(len(fname) < 1): fname = 'mbox-short'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '):continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts where email = ?',(email,))
    try:
        count = cur.fetchone()[0]
        cur.execute('UPDATE Counts SET count = count+1 where email =?',(email,))
    except:
        cur.execute(''' INSERT INTO Counts (email,count) values(?,1)''',(email,))

    conn.commit()

sqlstr = 'SELECT email,count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]),row[1])

cur.close()

