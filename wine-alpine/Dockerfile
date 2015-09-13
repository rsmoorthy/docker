FROM boggart/alpine-apk-static-32bit

MAINTAINER Moorthy "github.com/rsmoorthy"

LABEL description="Minimal alpine based wine. This is based on catataw/alpine-vnc-wine, but without vnc and others"

RUN ["/sbin/apk.static", "add", "--update", "alpine-base", "xvfb", "wine", "wget"]
RUN wget http://winetricks.org/winetricks && chmod +x winetricks && mv winetricks /usr/bin/winetricks
								    
ENV WINEARCH win32
ENV DISPLAY :0

# Default execute the entrypoint
CMD ["/bin/sh"]
