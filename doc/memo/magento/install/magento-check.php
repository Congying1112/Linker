<?php //header
	$header  = '';
	$footer  = '';
	$header  = '<!DOCTYPE html>';
	$header .= '<html dir="ltr" lang="zh">';
	$header .= '<head>';
	$header .= '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"  />';
	$header .= '<title>Magento系统需求测试</title>';
	$header .= '</head>';
	$header .= '<body>';
	$footer .= '</body>';
	$footer .= '</html>';
	echo $header;
?>
<?php
extension_check(array( 
	'curl',
	'dom', 
	'gd', 
	'hash',
	'iconv',
	'mcrypt',
	'pcre', 
	'pdo', 
	'pdo_mysql', 
	'simplexml'
));

function extension_check($extensions) {
	$fail = '';
	$pass = '';
	
	if(version_compare(phpversion(), '5.2.0', '<')) {
		$fail .= '<li>你需要<strong> PHP 5.2.0</strong> (或者更高)</li>';
	}
	else {
		$pass .='<li>你有<strong> PHP 5.2.0</strong> (或者更高)</li>';
	}

	if(!ini_get('safe_mode')) {
		$pass .='<li>安全模式<strong>关闭</strong></li>';
		preg_match('/[0-9]\.[0-9]+\.[0-9]+/', shell_exec('mysql -V'), $version);
		
		if(version_compare($version[0], '4.1.20', '<')) {
			$fail .= '<li>你需要<strong> MySQL 4.1.20</strong> (或者更高)</li>';
		}
		else {
			$pass .='<li>您有<strong> MySQL 4.1.20</strong> (或者更高)</li>';
		}
	}
	else { $fail .= '<li>安全模式是<strong>打开的</strong></li>';  }

	foreach($extensions as $extension) {
		if(!extension_loaded($extension)) {
			$fail .= '<li>你没有<strong>'.$extension.'</strong>扩展</li>';
		}
		else{	$pass .= '<li>你有<strong>'.$extension.'</strong>扩展</li>';
		}
	}
	
	if($fail) {
		echo '<p><strong>您的服务器不符合安装Magento的条件.</strong>';
		echo '<br>不符合下列<a href="http://www.magentochina.org/system-requirements" target="_blank">系统安装条件</a>，请联系主机商调整服务器环境以便运行Magento:';
		echo '<ul>'.$fail.'</ul></p>';
		echo '下面的条件已经满足:';
		echo '<ul>'.$pass.'</ul>';
	} else {
		echo '<p><strong>恭喜!</strong>您的服务器能的运行Magento.</p>';
		echo '<ul>'.$pass.'</ul>';
		echo '<footer>如果在安装Magento的过程中有任何疑问，可以看我们的<a href="http://www.magentochina.org/download-install" target="_blank">教程</a>或者去<a href="http://www.magentochina.org/bbs/" target="_blank">论坛提问</a>.</footer>';
	}
}
?>

<?php
	echo $footer;
?>