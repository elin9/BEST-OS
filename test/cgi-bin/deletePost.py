#!/usr/bin/python

import cgi
import cgitb
import sqlite3
import datetime
import os
import Cookie
import json
cgitb.enable()

t = str(datetime.datetime.now())

form = cgi.FieldStorage()
cookie_string = os.environ.get('HTTP_COOKIE')

conn = sqlite3.connect('BESTOS_DATABASE.db')
c = conn.cursor()

def main():
    aCookie = Cookie.SimpleCookie(cookie_string)
    username = aCookie['name'].value
    title = form.getvalue("title")
    
    #if cookie username matches form username?
    #if the book exists under the username?
    c.execute('delete from bookposts where user = ? and title = ?;', (username, title))
    conn.commit()
    conn.close()
    
    print("Content-type: text/html")
    print("")
    print("<html><head><title>Delete Post</title></head><body>")
    
    print("Deleted post<br>")
    print('Return to <a href="http://test.elin9.rochestercs.org/cgi-bin/index.php">home</a>.')
    print("</body></html>")

main()