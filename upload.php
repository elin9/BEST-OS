<?php
$upload_dir = "upload/";
$img = $_POST['file'];
// $user = $_POST['user'];
// $title = $_POST['title'];

// echo $img;

$types = array('jpg;','jpeg;','bmp;','png;');
// $temp = "";
foreach($types as $type){
	reset($types);
	if(strpos($img,$type) !== FALSE){
		$temp= $type;
		break;
	}
// 	else{
// 		echo "<script type='text/javascript'>alert('image type failed');</script>";
// 	}
}

$temp = str_replace(';','',$temp);
$temps='.' . $temp;

$str = 'data:image/' . $temp .';base64,';
$img = str_replace($str, '', $img);
$img = str_replace(' ', '+',$img);
// echo $img;
$data = base64_decode($img);
$file = $upload_dir . mktime() . $temps;
file_put_contents($file, $data);
chmod($file, 0777);
echo $file;
?>