<?php
$userconfig = "/boot/userconfig.txt";

require_once('controllers/StatusController.php');
require_once('controllers/SystemController.php');
require_once('controllers/ConfigController.php');
require_once('controllers/MeasureController.php');
require_once('controllers/ConvolverController.php');

$statusController = new StatusController();
$configController = new ConfigController($statusController, $userconfig);
$systemController = new SystemController($statusController);
$measureController = new MeasureController($statusController);
$convolverController = new ConvolverController($statusController, $configController);

// get the HTTP method, path and body of the request
$method = $_SERVER['REQUEST_METHOD'];
$request = explode('/', trim($_SERVER['REQUEST_URI'], '/'));

$input = json_decode(file_get_contents('php://input'), true);


switch ($method) {
case 'GET':
  $config = $configController->getValue();
  $system = $systemController->getValue();
  $measure = $measureController->getValue();
  $convolver = $convolverController->getValue();
  break;
case 'POST':
  switch($request[1]) {
  case 'save':
    $config = $configController->postValue($input);
    break;
  case 'convolver':
    // $convolver = $convolverController->postValue($input);
    break;
  case 'system':
    $system = $systemController->postValue($input);
    break;
  case 'measure':
    $measure = $measureController->postValue($input);
    break;
  }
  break;
default:
  break;
}

$status = $statusController->getValue();

$result = [
  "config" => $config,
  "convolver" => $convolver,
  "system" => $system,
  "measure" => $measure,
  "status" => $status,
];

header('Content-Type: application/json');
echo json_encode($result);

?>
