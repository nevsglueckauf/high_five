<?php

$st_lne = implode(' ', [$_SERVER['SERVER_PROTOCOL'], http_response_code(), ]);

?>

<pre>
<code>
<?php
 

if (count($_GET)) {
    print_r($_REQUEST);
} else {
    print 'No Data sent';
    
}
?>


</code>



</pre>