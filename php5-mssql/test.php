<?php

$dbh = new PDO("dblib:host=mssql;dbname=test", "sa", "");
$dbh->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
#
#$stmt = $dbh->prepare("insert t1 (id,name) Values (2,'world hello')");
#$stmt->execute();
#
$stmt = $dbh->prepare("select * from t1");
$stmt->execute();
$rows = $stmt->fetchAll();
print_r($rows);
