#!/usr/bin/python

import cgi
import cgitb
import os
import Cookie
import sqlite3

cgitb.enable()
form = cgi.FieldStorage()
cookie_string = os.environ.get('HTTP_COOKIE')

def main():
    usern = form.getvalue("username")
    formpass = form.getvalue("password")
    answ = form.getvalue("answer")
    
    print("Content-type: text/html")
    if cookie_string:
	deleteCookie()
    print("")
    print("<html><head><title>Delete Account</title>")
    if form.getvalue("answer") == "No":
    	redirectHead()
    print("</head>")
    print("<body>")
    if form.getvalue("answer") == "No":
    	redirectBody()
    elif form.getvalue("answer") == "Yes":
    	delete(usern)
        redirectHead()
    else:
    	if usern != None:
   	    pword = checkPassword(usern)
    	    if pword == formpass:
    	    	print("Do you really want to delete?<br>")
    	    	askIfSure(usern)
    	    else:
    	    	print("Password does not match! Try again.<br>")
    	    	deleteForm()
	else:
    	    deleteForm()
    print("</body></html>")

def askIfSure(un):
    print('<form method = post action = "deleteUsertry.py">')
    print('<input type=hidden name="username" value = "' + un +'">')
    print('<input type=submit name="answer" value="Yes">')
    print('<input type=submit name="answer" value="No"></form><br>')

def deleteForm():
    print("To delete account, enter username and password.<br>")
    print('<form method = post action = "deleteUsertry.py">')
    print('Username <input type = text name = "username"><br>')
    print('Password <input type = password name = "password"><br>')
    print('<input type=submit value="Submit">')
    print('<input type=reset value="Reset"></form><br>')

def redirectHead():
    print("""<meta charset="UTF-8">
        <meta http-equiv="refresh" content="1;url=http://elin9.rochestercs.org/">
        <script type="text/javascript">
            window.location.href = "http://elin9.rochestercs.org/"
        </script>""")

def redirectBody():
    print("If you are not redirected automatically, follow the <a href='http://elin9.rochestercs.org/'>link to home.</a>")

def checkPassword(username):
    conn = sqlite3.connect('BESTOS_DATABASE.db')
    c = conn.cursor()
    c.execute('select password from users where username = ?',(username,))
    p = str("%s" % c.fetchone())
    conn.close()
    return p

def delete(username):
    conn = sqlite3.connect('BESTOS_DATABASE.db')
    c = conn.cursor()
    c.execute('delete from users where username = ?',(username,))
    conn.commit()
    conn.close()
    
def deleteCookie():
  	aCookie = Cookie.SimpleCookie(cookie_string)
	aCookie['name']['expires'] = 'Thu, 01 Jan 1970 00:00:00 GMT'
	aCookie['current_time']['expires'] = 'Thu, 01 Jan 1970 00:00:00 GMT'
	aCookie['sessionID']['expires'] = 'Thu, 01 Jan 1970 00:00:00 GMT'
	print aCookie

main()