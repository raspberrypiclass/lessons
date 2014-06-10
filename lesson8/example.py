#!/usr/bin/env python

## the first line sets the http header that wil be returned
## this ends with two new line characters \n\n to indicate the
## end of the header string
print "Content-type: text/html\n\n"
## the second print statement sets the content of the http body
## remember the triple quote marks means the string can go
## over multiple lines
print """
Hello world
"""
