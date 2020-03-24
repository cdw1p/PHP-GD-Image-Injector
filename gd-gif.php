<?php

//php gd-gif.php image.gif gd-image.gif 

$gif = imagecreatefromgif($argv[1]);
imagegif($gif, $argv[2]);
imagedestroy($gif);
?>