<?php declare(strict_types=1);
/**
 * router.php - to be used with PHP Development Server 
 * 
 * Routes to `public/index.php`, if mapped (uri part <-> File system) resourse does not exist 
 *   
 * @author Sven Schrodt<sven@schrodt.club>
 * @link https://github.com/SchrodtSven/PhascolarctosCinereus
 * @package 
 * @version 0.1
 * @since 2025-03-16
 */


// if requested resource does not exist in file system:
if (!file_exists($_SERVER['DOCUMENT_ROOT'] . parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH))) { 
    $_SERVER['SCRIPT_NAME'] = 'index.php'; // setting up current script name in super global 
    require_once 'public/index.php'; // route to index.php
} else { // or just send existing resource
    return false;
}
