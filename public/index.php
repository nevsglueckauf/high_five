<?php
header('Content-Type: application/json');
require_once 'Reflector.php';
$r = new HttpReflector();

#var_dump($r);
$names = [];
$dta = require_once 'namesMails.php';

foreach ($dta as $p) {

    $item = new stdClass();
    $item->first_name = $p[0];
    $item->last_name = $p[1];
    $item->mail = $p[3];
    $names[] = $item;
}

$ffo = serialize($names);
file_put_contents('dta.ser', $ffo);

if (array_key_exists('list', $r->params)) {
    listMe();
} elseif (array_key_exists('user', $r->params)) {
    user();
} else {
    badReq();
}











date_default_timezone_set('Europe/Berlin');
$allowd_ctr = ['user', 'list'];


function listMe($a = 0)
{
    global $r;
    if ($r->m != 'GET') {
        e405();
    }
    global $names;
    $jnames = json_encode($names);
    #print $jnames;
    echo  $jnames;

    # print(__FUNCTION__);
    #print(PHP_EOL . $a);
}


function user($a = 0)
{
    global $names;
    global $r;

    $id = $r->params['id'] ?? null;
    switch ($r->m) {
        case 'PUT':
            action('Der User mit ID: ' . $id . ' wurde geändertt!');
            break;

            break;
        case 'GET':
            if (!is_null($id)) {
                $user = $names[$id] ?? null;
            }

            if ($id == null || $user == 'null') {
                e404();
            } else {
                print(json_encode($user));
            }
            break;

        case 'DELETE':
            action('Der User mit ID: ' . $id . ' wurde gelöscht!');
            break;

        case 'POST':
            action('Der neue User wurde angelegt!');
            break;

        default:
            e405();
    }
}

function action($msg)
{
    header('HTTP/1.1 200 OK');
    print(json_encode(['Message' => $msg]));
}

function badReq()
{
    resp('HTTP/1.1 400 Bad Request!');
}

function e404()
{
    resp('HTTP/1.1 404 File not found!');
}



function e405()
{
    resp('HTTP/1.1 405 Method Not Allowed!' . ' ' . $_SERVER['REQUEST_URI']);
}


function resp($st)
{
    header($st);
    print(json_encode(['Message' => $st]));
    exit();
}

# dispatch() ; 


#header('Content-Type: application/json');
#print($jnames);