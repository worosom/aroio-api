<?php
require_once('AbstractController.php');

class SystemController extends AbstractController {
  function getValue() {
    return $result;
  }

  function postValue($post) {
    if ($post['reboot']) {
      $this->status->postValue(StatusController::$REBOOTING);
      $this->reboot();
    }
    return $post;
  }

  function reboot() {
    // shell_exec('checksoundcard &');
    // shell_exec('sleep 5 && reboot -d 1 &');
    shell_exec('sleep 3 && echo "shutdown" &');
  }
}
?>
