var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var multer = require('multer')
// var upload = multer({dest: '/tmp'})
var upload = multer({storage: multer.memoryStorage()})

var api_key = "keys1234"
if(process.env.AUTH_KEY)
    api_key = process.env.AUTH_KEY

var urlencodedParser = bodyParser.urlencoded({ extended: false })
var jsonParser = bodyParser.json()

app.get('/', function (req, resp) {
    resp.status(400)
    resp.send("GET Method Unsupported")
})

var mfields = [{name: "files"}]
for(var i=1; i < 100; i++)
    mfields.push({name: "file" + i})

app.post('/js', upload.fields(mfields), function (req, resp) {
    if(!(req.headers.authorization == api_key || req.body.api_key == api_key))
        return errorResponse(resp, "Authorization failed")

    console.log(req.files)
    var jsString = "";
    for(var _file in req.files)
        for(var i in req.files[_file])
            jsString = jsString + req.files[_file][i].buffer.toString();

    var UglifyJS = require("uglify-js");
    var result = UglifyJS.minify(jsString, {fromString: true});
    console.log("Response length: " + result.code.length);
    resp.send(JSON.stringify({status: "ok", js: new Buffer(result.code).toString("base64")}))
})

app.post('/css', upload.fields(mfields), function (req, resp) {
    if(!(req.headers.authorization == api_key || req.body.api_key == api_key))
        return errorResponse(resp, "Authorization failed")

    console.log(req.files)
    var cssString = "";
    for(var _file in req.files)
        for(var i in req.files[_file])
            cssString = cssString + req.files[_file][i].buffer.toString();

    var UglifyCSS = require("uglifycss");
    var result = UglifyCSS.processString(cssString)
    console.log("Response length: " + result.length);
    resp.send(JSON.stringify({status: "ok", css: new Buffer(result).toString("base64")}))
})

app.post('/json', jsonParser, function (req, resp) {
    if(!(req.headers.authorization == api_key || req.body.api_key == api_key))
        return errorResponse(resp, "Authorization failed")
    resp.send('POST World');
})

var server = app.listen(80, function () {

    var host = server.address().address
    var port = server.address().port

    console.log("Example app listening at http://%s:%s", host, port)
})

function errorResponse(resp, err)
{
    resp.send(JSON.stringify({status: "error", error: err}))
}

exitOnSignal('SIGINT');
exitOnSignal('SIGTERM');
process.stdin.resume();

function exitOnSignal(signal) {
  process.on(signal, function() {
    console.log('\ncaught ' + signal + ', exiting');
    process.exit(1);
  });
}
