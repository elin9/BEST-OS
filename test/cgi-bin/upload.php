<?php
$upload_dir = "upload/";
$img = $_POST['file'];
$imgs = (string) $img;
$data = explode(';', $imgs,2);

$types = array('jpeg','bmp','png');
foreach($types as $type){
	if(strpos($data[0],$type) !== FALSE){
		$img = str_replace('data:image/{$type};base64,', '', $img);
		$img = str_replace(' ', '+', $img);
		$data = base64_decode($img);
// 		echo "what it looks like: $data";
		$file = $upload_dir . mktime() . ".png";
		$success = file_put_contents($file, $data);
		print $success ? $file : 'Unable to save the file.';
		exit;
	}
}
// 	if(strpos($img,$arr)!==false){
// // 	    echo $arr;
// 		
// 		
// 		
// 		echo $data;
// 		
// 		$success = file_put_contents($file, $data);
// 		print $success ? $file : 'Unable to save the file.';
// 		exit;
// 	}
// }

// echo $file;
// $img = str_replace('data:image/jpeg;base64,', '', $img);
// $img = str_replace(' ', '+', $img);
// $data = base64_decode($img);
// $file = $upload_dir . mktime() . ".{$type}";
// $success = file_put_contents($file, $data);
// print $success ? $file : 'Unable to save the file.';
?>