<!DOCTYPE html>
<head>
<meta charset="utf-8" />
<title>PHP Test</title>
</head>
<body>
<?php  

$fishes = array('tuna','mackerel','salmon','dog','cod');
$facts = array(' is a big fish',' has stripes',' migrates to spawn', ' is not a fish!',' makes a good sandwich');
foreach($fishes as $fish){
    if ($fish == "dog"){
        echo "Oh woof?</br>";
    }else{
        echo "Oh worm? </br>";
    }
}
while($fish = current($fishes)){
    echo "A ".$fish.current($facts)."</br>";
    next($fishes);
    next($facts);
}

?>

</body>