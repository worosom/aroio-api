<?php
require_once('StatusController.php');

abstract class AbstractController {
  function __construct($statuscontroller) {
    $this->status = $statuscontroller;
  }

  abstract protected function getValue();
  abstract protected function postValue($post);
}
?>
