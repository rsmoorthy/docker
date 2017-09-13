## Python Tools - Microservice

Currently this supports only one tool (microservice), which converts any "simple arithmetic like expression" (rather python expression)
and returns back the Mongo Query Like Value

### Synopsis

Build the tools like this:

```
docker build -t pythontools .
```

Run the python tools like this:

```
docker run --name pythontools -d -p 8000:80 pythontools
```

### Testing

```
curl http://localhost:8000/expr2mongo?expr=a==1
```

which returns

```
```

### Credits

* https://github.com/alonho/pql
