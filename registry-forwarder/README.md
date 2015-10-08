# Docker Registry Forwarder

Easily pull and push local private registries. The image is only 8MB in size

## Synopsis

Run the registry port forwarder, as follows:

```
docker run --name registry_forwarder -d -p 5000:5000 -e REGISTRY_HOST="<registry_host_ip>" -e REGISTRY_PORT="5000" rsmoorthy/registry-forwarder
```

Then pull or push images from your local registry:

```
docker pull localhost:5000/your-image
docker push localhost:5000/my-image
```

## Why this is needed?

Docker requires that the private registry supports SSL and proper certificates installed. In most cases, private registries are running within development environment 
and don't like to have certificates installed.

If you want to circumvent this, Docker requires --insecure-registry flag added to the daemon - which is again cumbersome, to be done in all clients.

The issue [https://github.com/docker/docker/issues/8887] requests that --insecure flag be added to docker pull command, but it is unlikely to be implemented for a while.

The above URL has a workaround as follows:

```
$ docker pull host:5000/image #fails
$ ssh -N -L 5000:host:5000 user@host
$ docker pull localhost:5000/image #works
```

But this would need a SSH account in the above host, and needs end users to run the SSH command from the boot2docker (in case of windows). And they have to make
the connection, everytime it disconnects.

The port forwarder helps solve the problem easily

## Credits

* elyase/staticpython for a super-small 8MB Python
* http://voorloopnul.com/blog/a-python-proxy-in-less-than-100-lines-of-code/ for a small TCP port forwarding code
