<!DOCTYPE html>
<html>
<head>
<title>try</title>
<link rel = "stylesheet" type = "text/css" href="style.css">
<script src="jquery-1.11.0.js"></script>
<script src="menu.js"></script>
</head>
<body>
	
	<h1>Homepage</h1>
	 <div id="header"></div>
        <div id="container">
            <div id="center" class="column" style="left: 80px;">middle</div>
            <div id="left" class="column">
            	<label for= "class" accesskey="c">Class</label>
					<select id="json-one">
					<br><pre><option selected value="base">Please Select a school</option></pre>
					<option value="Art">Arts Sciences and Engineering</option>
					<option value="Simon">Simon School of Business Administration</option>
					<option value="Warner">Warner School of Education</option>
					<option value="Eastman">Eastman School of Music</option>
					<option value="Medicine">School of Medicine and Dentistry</option>
				</select>
	
				<br/>
	
				<select id="json-two">
					<option>Please choose from above</option>
				</select>
				
			 </div>
             <div id="right" class="column">profile<br>
<?php
$cookie_name = "sessionID";
if(!isset($_COOKIE[$cookie_name])) {
    echo "Please <a href=\"http://elin9.rochestercs.org/cgi-bin/login.py\">login</a>.<br>";
} else {
    echo "<form method = post action = \"http://elin9.rochestercs.org/cgi-bin/deleteUser.py\">";
    echo "<input type=submit name = \"delete\" value = \"Delete your account\"></form>";
    echo "<form method = post action = \"http://elin9.rochestercs.org/cgi-bin/logout.py\">";
    echo "<input type = hidden name = \"sid\" value = " . $_COOKIE[$cookie_name] . ">";
    echo "<input type=submit name = \"logout\" value = \"Logout\"></form><br>";
}
?>
             </div>
    	</div>
        <div id="footer-wrapper">
              <div id="footer"></div>
        </div>
  
</body>
</html>