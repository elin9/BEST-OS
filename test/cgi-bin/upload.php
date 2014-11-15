<?php
  $name=$_POST['fd'];
  echo $name;
  $fp = fopen($name,'wb');
  fwrite($fp,$decodedData);
  fclose($fp);
   
//   $db = new SQLite3('cgi-bin/BESTOS_DATABASE.db') or die('Unable to open database');
//   $results = $db->query('SELECT * FROM bookposts') or die('Query failed');
//   while ($row = $results->fetchArray()) {
//     echo "User: {$row['courseNumber']}\nUsername: {$row['user']}\n";
//   }
?>