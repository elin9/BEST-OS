#!/usr/bin/env python

import cgi
import os
import cgitb
cgitb.enable()

print "hello"
    
form = cgi.FieldStorage()

img = form.getvalue("file")
txt = form.getvalue("txt")

print txt
print img

#fn = os.path.basename(img.filename)
#open('http://elin9.rochestercs.org/img/' + fn, 'wb').write(fileitem.file.read())
#message = 'The file "' + fn + '" was uploaded successfully.' + txt
   
#print """\
#Content-Type: text/html\n
#<html><body>
#<p>%s</p>
#</body></html>
#""" #% (message,)