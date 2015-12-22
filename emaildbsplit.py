__author__ = 'kwoshvick'
import sqlite3
import re

conn = sqlite3.connect('./databases/emaildbs.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'mbox-short'
fh = open(fname)
for line in fh:
    if not line.startswith('From: ') : continue
    pieces = line.split()
    emails = pieces[1]
    email_domain = re.findall('@([^ ]*)',emails)
    email = email_domain[0]
    #email_domain = emails.split('@')
    #email = email_domain[1]

    print (email)
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (email, ))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES ( ?, 1 )''', ( email, ) )
    else :
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?',
            (email, ))
    # This statement commits outstanding changes to disk each
    # time through the loop - the program can be made faster
    # by moving the commit so it runs only after the loop completes
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

print("Counts:")
for row in cur.execute(sqlstr) :
    print (str(row[0]), row[1])

cur.close()