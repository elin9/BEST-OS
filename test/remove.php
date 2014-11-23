<?php
$img = $_POST['photo'];
$img = str_replace('http://test.elin9.rochestercs.org/','',$img);
// $img = trim($img,'/upload');
// echo $img;
if (file_exists($img))
{
    unlink($img);
}
// See if it exists again to be sure it was removed
if (file_exists($img))
{
          echo "Problem deleting " . $img;
}
else
{
        echo "Successfully deleted " . $img;
}
?>

?>