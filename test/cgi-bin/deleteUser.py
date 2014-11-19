#!/usr/bin/python

import cgi
import cgitb
cgitb.enable()
import sqlite3
form = cgi.FieldStorage()

def main():
    usern = form.getvalue("username")
    formpass = form.getvalue("password")
    answ = form.getvalue("answer")
    
    print("Content-type: text/html")
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
    print('Return to <a href="http://test.elin9.rochestercs.org/cgi-bin/index.php">home</a>.')
    print("</body></html>")

def askIfSure(un):
    print('<form method = post action = "deleteUsertry.py">')
    print('<input type=hidden name="username" value = "' + un +'">')
    print('<input type=submit name="answer" value="Yes">')
    print('<input type=submit name="answer" value="No"></form><br>')

def deleteForm():
    print('<form method = post action = "deleteUsertry.py">')
    print('<fieldset><legend>To delete account, enter username and password.</legend>')
    print('Username <input type = text name = "username"><br>')
    print('Password <input type = password name = "password"><br>')
    print('<input type=submit value="Submit">')
    print('<input type=reset value="Reset"></fieldset></form><br>')

def redirectHead():
    print("""<meta charset="UTF-8">
        <meta http-equiv="refresh" content="1;url=http://test.elin9.rochestercs.org/cgi-bin/index.php">
        <script type="text/javascript">
            window.location.href = "http://test.elin9.rochestercs.org/cgi-bin/index.php"
        </script>""")

def redirectBody():
    print("If you are not redirected automatically, follow the <a href='http://test.elin9.rochestercs.org/cgi-bin/index.php'>link to home.</a>")

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

main()