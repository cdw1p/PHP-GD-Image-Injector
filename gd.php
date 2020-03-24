<?php

//php gd.php image.jpg gd-image.jpg 0-100[optional]

(isset($argv[3]) ? $q = $argv[3] : $q = -1);
$jpg = imagecreatefromjpeg($argv[1]);
//imagejpeg ( resource $image [, mixed $to = NULL [, int $quality = -1 ]] ) : bool
imagejpeg($jpg, $argv[2], $q);
imagedestroy($jpg);
?>