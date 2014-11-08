#!/usr/bin/python

import cgi
import cgitb
cgitb.enable()
import sqlite3
form = cgi.FieldStorage()

def main():
    conn = sqlite3.connect('BESTOS_DATABASE.db')
    c = conn.cursor()
    usern = form.getvalue("username")
    email = form.getvalue("email")
    indb = checkUn(c,usern)
    emindb = checkEm(c,email)
    password = form.getvalue("password")
    password2 = form.getvalue("password2")
    
    print("Content-type: text/html")
    print("")
    print("<html><head><title>create account</title>")
    print("</head><body>")    
    if usern == None:
    	formBody()
    elif str(indb) != "None":
    	print("Username is taken!<br>")
        formBody()
    elif str(emindb) != "None":
    	print("Account already exists with this email!<br>")
        formBody()
    elif password != password2:
    	print("The passwords you entered do not match!<br>")
    	formBody()
    else:
    	databIn(c,usern,form.getvalue("password"),email)
    	conn.commit()
    	print("Your username: " + str(usern) + "<br>")
    	print("Your password: " + str(form.getvalue("password")) + "<br>")
    	print("Your email: " + str(email) + "<br>")
    print('Return to <a href="http://elin9.rochestercs.org">home</a>.')
    print("</body></html>")
    conn.close()

def databIn(c, un, ps, em):
    c.execute('insert into users values(?,?,?,?)', (un, ps, em, None))

def checkUn(c,variable):
    c.execute('select username from users where username = ?',(variable,))
    return str("%s" % c.fetchone())
    
def checkEm(c,variable):
    c.execute('select username from users where username = ?',(variable,))
    return str("%s" % c.fetchone())

def formBody():
    print("""<form name = "frm" method = post action = "form.py">
<fieldset>
<legend>Create new account</legend>
Username: <input type = text id = "un" name = "username" required><br>
Password: <input type = password id = "pw" name = "password" required><br>
Re-enter password:  <input type password id = "pw2" name = "password2" required><br>
Email: <input type = text id = "em" name = "email" required><br>
<br>
<input type=submit value="Submit">
<input type=reset value="Reset">
</fieldset>
</form>""")

main()