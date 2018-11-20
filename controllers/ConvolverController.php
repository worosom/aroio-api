<?php
require_once('AbstractController.php');

//Browse Directory and return array
function browseDirectory($directory)
{
	if ($handle = opendir($directory)) {
	    while(false !== ($entry = readdir($handle)))
	    {
	        if ($entry != "." && $entry != "..") $dirArr.=$entry.' ';
	    }
	    closedir($handle);
	    return $dirArr;
	}
	else return null;
}


class ConvolverController extends AbstractController {
  function __construct($statusController, $configController) {
    parent::__construct($statusController);
    $this->config = $configController->getValue();
  }
	//liest die Filter aus Pfad aus
	function getFilters()
	{
		$directory = '/boot/filter'; //evtl als konstante bzw in config-file
		if ($regexString=browseDirectory($directory)) {
				/*while(false !== ($entry = readdir($handle)))
				{
						if ($entry != "." && $entry != "..") $regexString.=$entry.' ';
				}
				closedir($handle);*/
			$rate=(int)($this->config['RATE'] / 1000);
			//$pattern = "/(\\w*)L|R(\\d*).dbl/";
			$pattern = "/(\\w*)(L|R)".$rate.".dbl/";
			//check if surround
			if ($this->config['CHANNELS']==4) {
				$pattern = "/(\\w*)S(L|R)".$rate.".dbl/";
			}
			preg_match_all($pattern, $regexString, $banks); // in $banks[1] Coeffset-Name
			$result = array_unique($banks[1]);
			$out= [];
			foreach ($result as &$option) {
        array_push($out, $option);
			}
			return $out;
		}
	}
  function getValue() {
    $result = [
      "choices" => $this->getFilters()
    ];
    return $result;
  }

  function postValue($post) {
    return $result;
  }
}
?>
