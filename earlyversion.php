<!DOCTYPE html> 

<html> 
<head> 
<style type="text/CSS"> 
	body{ } 
</style> 
</head> 
<body> 
<h1>BEST-OS</h1> 
<h2>Buying/Exchanging/Selling Textbooks (and Other Stuff)</h2> 


<?php
$cookie_name = "sessionID";
if(!isset($_COOKIE[$cookie_name])) {
    echo "Cookie named '" . $cookie_name . "' does not exist!<br>";
    echo "<a href=\"http://elin9.rochestercs.org/cgi-bin/form.py\">Create an account</a><br>";
    echo "<a href=\"http://elin9.rochestercs.org/cgi-bin/login.py\">Login</a><br>";
} else {
    echo "Cookie is named: " . $cookie_name . "<br>Value is: " . $_COOKIE[$cookie_name] . "<br>";
    echo "<form method = post action = \"cgi-bin/deleteUser.py\">";
    echo "<input type=submit name = \"delete\" value = \"Delete your account\"></form>";
    echo "<form method = post action = \"cgi-bin/logout.py\">";
    echo "<input type = hidden name = \"sid\" value = " . $_COOKIE[$cookie_name] . ">";
    echo "<input type=submit name = \"logout\" value = \"Logout\"></form><br>";
}
?><br>

<a href="http://elin9.rochestercs.org/cgi-bin/printDB.py">View the database</a><br> 
<a href="http://elin9.rochestercs.org/cgi-bin/deleteAll.py">Delete all accounts</a> (click only if you mean it)<br> 

</body> 
</html>