#!/usr/bin/python

import cgi
import cgitb
cgitb.enable()
import sqlite3

def main():
    print("Content-type: text/html")
    print("")
    conn = sqlite3.connect('BESTOS_DATABASE.db')
    c = conn.cursor()
    for row in c.execute('select * from bookposts'):
    	print "User: %s | Title: %s | Author: %s | Edition: %s | ISBN: %s | Condition: %s | Other Notes: %s | Course Number: %s | Photo: %s | Price: %s" % row
    	print("<br>")
    print "<br>"
    conn.close()

main()