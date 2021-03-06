<!DOCTYPE html>
<html>
<head>
	<title></title>
	<link href="https://fonts.googleapis.com/css2?family=MuseoModerno:wght@500&family=Roboto&display=swap" rel="stylesheet"> 
	<script type="text/javascript" src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
	<style type="text/css">
		body {
			background: #1fde6e;
			margin: 0;
			font-family: 'Roboto', sans-serif;
			text-align: center;
		}

		.nav {
			background-color: #de1f1f;
			top: 0;
			position: fixed;
			color:white;
			width:100%;
		}

		.container {
			font-family: 'MuseoModerno', cursive;
			margin-top: 10em;
		}

		.footer {
			position: fixed;
			bottom: 0;
			padding-left: 10px;
		}

	</style>
	<meta charset="utf-8">
	<meta name="description" content="Handahófskenndar setningar á íslensku.">
	<meta name="keywords" content="random, setningar, íslenska, icelandic">
	<meta name="author" content="Óliver Máni">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta property="og:title" content="Handahófskenndar Setningar á Íslensku!" />
	<meta property="og:site_name" content="RandomSetningar">
	<meta property="og:description" content="Vefsíða sem býr til handahófskenndar setningar á íslensku!" />
	<meta property="og:locale" content="is_IS">
</head>
<body>
	<div class="nav">
		<h1>Handahófskenndar setningar...</h1>
	</div>
	<div class="container">
		<h1 id="setning"></h1>
		<button onclick="renew()">Ný setning</button>

		<script type="text/javascript">
			function renew() {
				document.getElementById('setning').innerHTML = "<span style=\"color:red\">Bý til setningu...</span>";
				$.getJSON('/random', function(data){
					document.getElementById('setning').innerHTML = data.text;
				});
			}

			renew();
			
		</script>
	</div>
	<div class="footer">
		<p>Búið til af <a href="https://olivermani.com/" target="_blank">Óliver Mána</a>, kóði: <a href="https://github.com/OliverMani/HandahofsSetningar">https://github.com/OliverMani/HandahofsSetningar</a></p>
	</div>
</body>
</html>