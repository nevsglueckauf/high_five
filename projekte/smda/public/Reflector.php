<?php
/**
 * Reflecting HTTP request data - headers, payload
 *  
 * - public attributes 😛 (members) for convenience 😛
 * 
 * Author: Sven Schrodt
 * Since: 2025-06-03
 */

class HttpReflector
{
    public string $m, $qs, $acc, $prot, $uri;

    public array $params;

    protected array $payloadParam = ['PATCH', 'PUT'];

    protected array $fromStdin = [];

    public function __construct()
    {
        // Reading data from <STDIN> for methods ! being POST, or GET (that sit on $_GET, $_POST)
        parse_str(file_get_contents('php://input'), $this->fromStdin);

        // Setting public attributes
        $this->m  = $_SERVER['REQUEST_METHOD'] ?? '';
        $this->qs = $_SERVER['QUERY_STRING']   ?? '';
        $this->acc = $_SERVER['HTTP_ACCEPT']   ?? '';
        $this->prot = $_SERVER['SERVER_PROTOCOL']   ?? '';
        $this->uri = $_SERVER['REQUEST_URI']   ?? '';
        $this->params = $_REQUEST ?? [];

        if ($this->m == 'DELETE') {

            $this->params = array_merge($this->fromStdin);
        }

        if ($this->m == 'POST') $this->params = array_merge($this->params, $_POST);

        if (in_array($this->m, $this->payloadParam)) {
            $this->params = array_merge($this->params, $this->fromStdin);
        }
    }

    public function init(): void
    {
        print PHP_EOL;
        print ('You sent a request via ') . $this->m;
        print PHP_EOL;
        if (count($this->params)) {
            var_dump($this->params);
        }
    }


    public function dmp(): void
    {
        foreach ($_SERVER as $k => $v) {
            print(implode(' ', [$k, $v]) . PHP_EOL);
        }
    }

    public function reqH(): string
    {
        $rh = [implode(' ', [$this->m, $this->uri, $this->prot])];
        print_r($_SERVER);
        $req = array_merge($rh, getallheaders());
        $tmp = '';
        foreach ($req as $k => $v) {
            if ($k == '0') print $v . PHP_EOL;
            else $tmp .= "$k: $v" . PHP_EOL;
        }
        return $tmp;
    }
}
