#!/usr/bin/env python
import MySQLdb

db = MySQLdb.connect("localhost", "root", "pi", "rpi")
curs=db.cursor()

curs.execute ("SELECT * FROM students")

## the first line sets the http header that wil be returned
## this ends with two new line characters \n\n to indicate the
## end of the header string
print "Content-type: text/html\n\n"
## the second print statement sets the content of the http body
## remember the triple quote marks means the string can go
## over multiple lines
print """
Database results<br /><br />
"""

for reading in curs.fetchall():
	print "<h1>%s %s</h1><br />" % (str(reading[0]),str(reading[1]))

db.close()
