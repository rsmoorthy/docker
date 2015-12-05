## Uglify as a service

Uglify (Combine and Compress) JS and CSS Files

### Synopsis

Run the uglify as a service

```
docker run --name uglify -d -p 80:80 -e AUTH_KEY="keys1234" rsmoorthy/uglify-aas
```

To access it,

```
echo "var w = 'hello world';" > file1.js
echo "console.log(w);" > file2.js
```

Run it as 

```
curl -F files=@file1.js -F files=@file2.js -X POST -H 'Authorization: keys1234' localhost:9001/js
```

resulting in  (base64 encoded output)
```
{"status":"ok","js":"dmFyIHc9ImhlbGxvIHdvcmxkIjtjb25zb2xlLmxvZyh3KTs="}
```

Again run it as:

```
curl -s -F files=@file1.js -F files=@file2.js -X POST -H 'Authorization: keys1234' localhost:9001/js | sed 's/.*js\":\"\(.*\)\".*/\1/' | base64 -d
```

resulting in

```
var w="hello world";console.log(w);
```

