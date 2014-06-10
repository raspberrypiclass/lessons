#!/usr/bin/env python
import MySQLdb
import cgi

## set up connection to database
db = MySQLdb.connect("localhost", "root", "pi", "rpi")
curs=db.cursor()
##access POST variables send through form
form = cgi.FieldStorage()

##set header content type and two new lines to end header
print "Content-type: text/html\n\n"
try:
## create python variables from the POST variables sent through the form
   firstname = form["firstname"].value
   secondname = form["secondname"].value
## this line inserts the values from the form in to the database
   curs.execute("INSERT INTO students VALUES('%s','%s')" % (firstname,secondname))
   db.commit()
except:
   print "Error"

print "Database updated"

db.close()
