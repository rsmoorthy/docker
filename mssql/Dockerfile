FROM rsmoorthy/sql2000

MAINTAINER Moorthy "github.com/rsmoorthy"

LABEL description="Provides MSSQL 2000 (Microsoft SQL Server 2000 Desktop Engine (MSDE 2000) Release A). If you want to run MSSQL 2000 as a database server, ONLY using the 1433 port, you can make use of this docker image. Service is available on port 1433, user sa, empty password"

LABEL alias="This is alias for rsmoorthy/sql2000"

LABEL how.installed="For details on this image was created, Please refer to github.com/rsmoorthy/dockerfiles/sql2000/how_installed.md"

ENV WINEARCH win32
ENV DISPLAY :0

# Expose the default port
EXPOSE 1433 

# Default execute the entrypoint
CMD ["/bin/sh", "root/start.sh"]
