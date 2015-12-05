<?php

chdir("/tmp");

function _errormsg($string)
{
	error_log("error: $string");
	print json_encode(array("status"=>"error", "error"=>$string));
	exit;
}

function getTempFile($prefix="random", $format="")
{
	$file = tempnam("/tmp", $prefix);
	if($format == "")
		return $file;
	rename($file, "$file.$format");
	return "$file.$format";
}

if(empty($_REQUEST["contents"]) or empty($_REQUEST["format"]))
	_errormsg("Invalid params");

$format = $_REQUEST["format"];
$input_format = $_REQUEST["input_format"];
$options = $_REQUEST["options"];
$contents = $_REQUEST["contents"];
$filename = $_REQUEST["filename"];

if($format == "pdf" and $input_format == "html") {
	$infile = getTempFile("html", "html");
	$outpdf = getTempFile("pdfout", "pdf");
	$contents = base64_decode($contents);
	file_put_contents($infile, $contents);

	exec("wkhtmltopdf $options $infile $outpdf");
	$response = file_get_contents($outpdf);
	unlink($infile);
	unlink($outpdf);
	if(!$response)
		_errormsg("Could not convert using wkhtmltopdf");
	print json_encode(array("status"=>"ok", "$format"=>base64_encode($response)));
	exit;
}

$formats = array("jpg", "jpeg", "png");
if(in_array($format, $formats) and $input_format == "pdf") {
	$infile = getTempFile("pdf", "pdf");
	$outimg = "imgout.$format";
	$contents = base64_decode($contents);
	file_put_contents($infile, $contents);

	$fmt = $format;
	if($format == "jpg")
		$fmt = "jpeg";
	exec("pdftoppm -$fmt -singlefile -rx 75 -ry 75 $infile imgout");
	$response = file_get_contents($outimg);
	unlink($infile);
	unlink($outpdf);
	if(!$response)
		_errormsg("Could not convert using pdftoppm");
	print json_encode(array("status"=>"ok", "$format"=>base64_encode($response)));
	exit;
}

$formats = array("jpg", "jpeg", "png", "gif");
if(in_array($format, $formats) and $input_format == "html") {
	$infile = getTempFile("html", "html");
	$outimg = getTempFile("imgout", $format);
	$contents = base64_decode($contents);
	file_put_contents($infile, $contents);

	exec("wkhtmltoimage $options $infile $outimg");
	$response = file_get_contents($outimg);
	unlink($infile);
	unlink($outimg);
	if(!$response)
		_errormsg("Could not convert using wkhtmltoimage");
	print json_encode(array("status"=>"ok", "$format"=>base64_encode($response)));
	exit;
}

if($format == "pdfunite") {
	// Content is json_encoded array
	$pdf_contents = json_decode($contents);
	if(!$pdf_contents)
		_errormsg("Invalid contents for pdfunite");
	$infiles = array();
	foreach($pdf_contents as $encodedPdf) {
		$file = getTempFile("pdfin", "pdf");
		$decoded = base64_decode($encodedPdf);
		if(!$decoded)
			_errormsg("Unable to obtain one of the incoming pdf files for pdfunite");
		file_put_contents($file, base64_decode($encodedPdf));
		$infiles[] = $file;
	}

	$pdfs = implode(" ", $infiles);
	$outpdf = getTempFile("pdfout", "pdf");
	exec("pdfunite $pdfs $outpdf");
	foreach($infiles as $ifile)
		unlink($ifile);
	$response = file_get_contents($outpdf);
	if(!$response)
		_errormsg("Could not convert using pdfunite");
	unlink($outpdf);
	print json_encode(array("status"=>"ok", "$format"=>base64_encode($response)));
	exit;
}
_errormsg("invalid formats");


