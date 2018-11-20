<?php
class StatusController {
  public static $LOADING = 'loading';
  public static $SAVING = 'config_saving';
  public static $SAVED = 'config_saved';
  public static $REBOOT = 'reboot';
  public static $REBOOTING = 'rebooting';
  public static $IDLE = 'idle';

  function __construct() {
    $this->status = StatusController::$LOADING;
  }

  function getValue() {
    return $this->status;
  }

  function postValue($post) {
    $this->status = $post;
    return $this->getValue();
  }
}
?>
