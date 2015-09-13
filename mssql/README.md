# MSSQL Database (SQL 2000)

MSSQL Database (SQL 2000) (Microsoft SQL Server 2000 Desktop Engine (MSDE 2000) Release A). 

If you want to run MSSQL 2000 as a database server, ONLY using the 1433 port, you can make use of this docker image. 

**Database Service is available on port 1433, user sa, empty password.**

This runs on top of rsmoorthy/wine-alpine, a minimal Wine installation on top of alpine 32bit. Credits for setting up MSSQL 2000 on top of Wine goes to https://appdb.winehq.org/objectManager.php?sClass=version&iId=11016

## Usage

```
docker run --name mssql -p 1433:1433 -d rsmoorthy/mssql
```

From any of the clients, connect to the service on the port 1433, user is "sa" and empty password


To test from a php5 client, you can run this:

```
docker run --rm -it --link mssql:mssql rsmoorthy/php5-mssql php /root/test.php
```

which displays 
```
Array
(
    [0] => Array
        (
            [id] => 1
            [0] => 1
            [name] => hello world
            [1] => hello world
        )

)
```

For Building and creating this image, please see this link https://github.com/rsmoorthy/docker/blob/master/sql2000/how_installed.md
