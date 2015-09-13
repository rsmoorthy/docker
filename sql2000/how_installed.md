# How the installation was done

The actual wine installation along with MSSQL 2000 cannot be installed using the Docker process, since the installation of SQL 2000 and prerequisites require manual intervention.

So, the installation is done (using the following steps) and the .wine folder copied to this image during the build.

```
$ rm -rf ~/.wine
$ export WINEARCH=win32
$ export WINEPREFIX=~/.wine
$ winetricks winxp
$ winetricks mdac28
```

Now download MSDE2000A.exe from http://www.microsoft.com/en-in/download/details.aspx?id=22661 into /tmp
Here the tips from https://appdb.winehq.org/objectManager.php?sClass=version&iId=11016 is followed

```
$ wine /tmp/MSDE2000A.exe
# Wait for this command to complete
$ wine ~/.wine/drive_c/MSDERelA/setup.exe DISABLEROLLBACK=1 BLANKSAPWD=1 DISABLENETWORKPROTOCOLS=0 SECURITYMODE=SQL
# It will exit with errors, which is fine
$ cp ~/.wine/drive_c/users/{username}/Temp/SqlSetup/Temp/* ~/.wine/drive_c/windows/system32/
```

For testing, Running the sqlmanager will start the SQL2000: (this is accomplished by the start.sh in the Docker image)
```
$ wine ~/.wine/drive_c/Program\ Files/Microsoft\ SQL\ Server/80/Tools/Binn/sqlmangr.exe
```

After this, the following steps are done to clean up .wine folder to reduce the size from 400MB to 105MB

```
$ cd ~/.wine/drive_c
$ rm -rf MSDERelA    # This folder is not needed, after installation
$ rm -rf windows/Installer # Deleted some installer files
$ rm -rf windows/system32/gecko # These files were probably copied, because my wine installation had wine-gecko installed
$ rm -rf windows/mono # These files were probably installed, because my wine installation had wine-mono installed
```

Using the Studio Express, I have created the databases "test" and "mine"
