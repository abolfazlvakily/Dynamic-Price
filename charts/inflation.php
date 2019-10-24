<!DOCTYPE html>
<html lang="en">
<head>
  <title>Dynamic Price - The Perch</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
  <script src="inflate.js"></script>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
</head>
<body>

<div class="container">
  <h2>Dynamic Price</h2><br><hr/>
  <a href="price.php"><button type="button" class="btn">Market Price Analysis</button></a>
  <a href="https://api.nodal.direct/v1/index.php/Api/ViewPerchPrice"><button type="button" class="btn btn-primary">Live Perch Price forecast</button></a>
</div><hr/>
<div id="chartContainer" style="height: 500px; width: 100%;"></div>
<script src="https://canvasjs.com/assets/script/canvasjs.min.js"></script>
</body>
</html>