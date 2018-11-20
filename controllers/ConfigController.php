<?php
require_once('AbstractController.php');

class ConfigController extends AbstractController {
  function __construct($statuscontroller, $userconfig) {
    parent::__construct($statuscontroller);
    $this->userconfig = $userconfig;
  }

  function getValue() {
    return parse_ini_file($this->userconfig, true);
  }

  function postValue($post) {
  //	$shell_exec_ret=exec('cardmount rw');
    $file = $this->userconfig;
    $content = file_get_contents($file);
    foreach ($post as $key => $value) {
      foreach ($value as $varName => $value) {
        $content = $this->replaceVariable($content, $varName, $value);
      }
    }
    file_put_contents($file, $content);
  //	$shell_exec_ret=exec('cardmount ro');
    $this->status->postValue(StatusController::$IDLE);
    return $this->getValue();
  }

  // Liest die Userconfig bis zur veraenderten Variable
  // und schreibt sie in das File
  function replaceVariable($content, $varName,$value) {
    $value=strval($value);
    $pattern ='/'.$varName.'=\".*\"/';
    return preg_replace($pattern, $varName.'="'.$value.'"', $content);
  }
}
?>
