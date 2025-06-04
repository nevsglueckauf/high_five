<?php
require_once 'Reflector.php';
date_default_timezone_set('Europe/Berlin');
$r = new HttpReflector();
?>
<!DOCTYPE html>
<html>
<head>
<title><?=$r::class?> sayz @<?=date('y-m-d H:i:s')?>:</title>
</head>
<body>
<pre>
<code><?=$r->init();?>
</code>
</pre>
<hr>
<pre>
    <kbd><?=$r->reqH()?></kbd>
</pre>
</body>
</html>