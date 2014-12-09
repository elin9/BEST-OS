<?php
	$db = new SQLite3('cgi-bin/BESTOS_DATABASE.db');
	$results = $db->query('SELECT photo FROM bookposts');
	$row = array();
	$i=0;
	while ($res = $results->fetchArray(SQLITE3_ASSOC)){
		if(!isset($res['photo'])) continue;
		$row[$i] = $res['photo'];
		$i++;
	}
	
	
	$file=scandir('upload/');
	$file = array_map(function($val) { return 'http://elin9.rochestercs.org/upload/'.$val; }, $file);
	$result = array_diff($file, $row);
	
	foreach ($result as $img) {
		$img = str_replace('http://elin9.rochestercs.org/','',$img);
		$img = getcwd() . "/" . $img;
// 		print $img . "<br>";
		unlink($img);
		if (file_exists($img))
		{
    		unlink($img);
//     		print $img . "<br>";
		}	
// 		 
	}
	
// 	print getcwd() . "\n";
	
?>