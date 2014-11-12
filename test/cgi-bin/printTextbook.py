#!/usr/bin/python

import cgi
import cgitb
cgitb.enable()
import sqlite3

form = cgi.FieldStorage()

def main():
    print("Content-type: text/html")
    print("")
    conn = sqlite3.connect('BESTOS_DATABASE.db')
    c = conn.cursor()
    school = form.getvalue("school")
    course = form.getvalue("course")
    schoolFilter = None
    courseFilter = None

    if str(school)== "None" or str(school) == "base":
    	for row in c.execute('select * from bookposts order by datePosted desc'):
    	    print "<div class = \"post\" style = \"border: 1px solid #000000; height: 100px;\">Seller: %s | Title: %s | Author: %s | Edition: %s | ISBN: %s | Condition: %s | Other Notes: %s | Course Number: %s | <img style = \"width: 50px; height: 70px; float: left;\" src = \"%s\"> Price: $%s | School: %s | Course: %s | Date Posted: %s GMT </div>" % row
    	    print("<br><br>")
    else:
        print "Showing textbooks for " + str(school) + " " + str(course) + ":<br><br>"
    	for row in c.execute('select * from bookposts where school = ? and course = ? collate nocase order by datePosted desc;',(str(school),str(course))):
    	    print "<div class = \"post\" style = \"border: 1px solid #000000; height: 100px;\">Seller: %s | Title: %s | Author: %s | Edition: %s | ISBN: %s | Condition: %s | Other Notes: %s | Course Number: %s | <img style = \"width: 50px; height: 70px; float: left;\" src = \"%s\"> Price: $%s | School: %s | Course: %s | Date Posted: %s GMT </div>" % row
    	    print("<br><br>")
    conn.close()

main()