#!/usr/bin/python

import cgi
import cgitb
cgitb.enable()
import sqlite3

def main():
    print("Content-type: text/html")
    print("")
    print("<html><head><title>print database</title></head>")
    print("<body>")
    print("username, password, email, session id<br><br>")
    conn = sqlite3.connect('BESTOS_DATABASE.db')
    c = conn.cursor()
    for row in c.execute('select * from users'):
    	print "%s, %s, %s, %s" % row
    	print("<br>")
    conn.close()
    print('<br>Return to <a href="http://elin9.rochestercs.org/">home</a>.')
    print("</body></html>")

main()