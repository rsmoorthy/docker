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
curl http://localhost:8000/SchemaFreeParser?expr=a==1
{"a": 1}
```


```
curl -G "localhost:8000/SchemaFreeParser" --data-urlencode "expr=(a == 1) and (b > 2)"
{"$and": [{"a": 1}, {"b": {"$gt": 2}}]}
```

```
curl -G "localhost:8000/AggregationParser" --data-urlencode "expr=(a == 1) and (b > 2)"
{"$and": [{"$eq": ["$a", 1]}, {"$gt": ["$b", 2]}]}
```

### Credits

* https://github.com/alonho/pql
