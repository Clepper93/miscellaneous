<!DOCTPYE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>PHP Test</title>
</head>
<body>
<h2>Fun with PHP</h2>
<?php 
$counter = 0;
while($counter<=10){
    if ($counter % 2 == 0){
        echo "$counter is even" . "<br>";
    } else{
        echo "$counter is odd"."<br>";
    }
$counter++;
}
?>
</body
