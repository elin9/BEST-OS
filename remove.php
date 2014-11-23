<?php
$img = $_POST['photo'];
$img = str_replace('http://elin9.rochestercs.org/','',$img);
// $img = trim($img,'/upload');
// echo $img;
if (file_exists($img))
{
    unlink($img);
}

?>

?>