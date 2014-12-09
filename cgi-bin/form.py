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
    print("<html><head><title>Create account</title>")
    print '<style>'
    print """body {
    background:url('http://cdn1.bigcommerce.com/n-ww20x/1n77e/products/1905/images/2848/library_bookcase_wallpaper__69506.1407915090.1280.1280.jpg?c=2'); 
    height:70%;
    text-align:center;
    color:#fff;
    font-size:16px;
    font-family:sans-serif;
}
h2{
    text-align:center;
}
a{
	color:#fff;
	font-weight:bold;
	font-size:20px;
	text-decoration:none;
}
form{
    color:#fff;
}
table{
    background:rgba(255,255,255,0.7);
    margin-left:auto;
    margin-right:auto;
    border:none;
    border-radius:10px;
    padding:3em;
    width:100px;
    height:100px;
    color:#000;
}
td{
    width:10%;
    
}

input[type="submit"],input[type="reset"]{
    border:none;
    width:80px;
    height:30px;
	margin-top:30px;
    background:rgba(255,255,255,0.9);
    border-radius:10px;
    font-size:10pt;
}

input[type="reset"]{
    margin-left:58px;
}

input[type="text"],input[type="password"]{
    font-size:18pt;
    width:150px;
    height:50px;
}"""
    print '</style>'
#     print('<link rel = "stylesheet" type = "text/css" href="http://elin9.rochestercs.org/experimenting/style2.css">')
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
    	print("Hooray! Congrats, " + str(usern) + ", you have created an account with the following email address:<br>")
    	print(str(email) + "<br><br>")
    print('Return <a href="http://elin9.rochestercs.org/cgi-bin/index.php">home</a> to login.')
    print("</body></html>")
    conn.close()

def databIn(c, un, ps, em):
    c.execute('insert into users values(?,?,?,?)', (un, ps, em, None))

def checkUn(c,variable):
    c.execute('select username from users where username = ?',(variable,))
    return str("%s" % c.fetchone())
    
def checkEm(c,variable):
    c.execute('select username from users where email = ?',(variable,))
    return str("%s" % c.fetchone())

def formBody():
    print("""<form name = "frm" method = post action = "form.py">
<table>
<h2>Create a new account</h2>
<tr><td>Username: </td><td><input type = text id = "un" name = "username" required></td></tr>
<tr><td>Password: </td><td><input type = password id = "pw" name = "password" required></td></tr>
<tr><td>Re-enter password: </td><td><input type= password id = "pw2" name = "password2" required></td></tr>
<tr><td>Email: </td><td><input type = text id = "em" name = "email" required><br></td></tr>
<tr>
<td colspan="3"><input type=submit value="Submit">
<input type=reset value="Reset"></td>
</tr>
</table>
</form>""")

main()