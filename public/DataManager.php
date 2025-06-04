<?php

class DataManager implements \Countable, \ArrayAccess
{
    public array $dta = [];

    public function __construct(private string $fn = 'dta.ser')
    {
        $this->dta = unserialize(file_get_contents($this->fn));
    }

    public function count(): int
    {
        return count($this->dta);
    }

   public function offsetGet($offset): mixed
    {
        return $this->dta[$offset] ?? null;
    }

    public function offsetSet($offset, $value): void
    {
        if (is_null($offset)) {
            $this->dta[] = $value;
        } else {
            $this->dta[$offset] = $value;
        }
    }

    public function offsetExists($offset): bool
    {
        return isset($this->dta[$offset]);
    }

    public function offsetUnset($offset): void
    {
        unset($this->dta[$offset]);
    }

}


$foo = new DataManager();


print_r($foo->count());

print_r($foo[3]);