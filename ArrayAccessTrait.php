<?php

declare(strict_types=1);
/**
 * Trait for classes implementing interface \ArrayAccess
 * 
 * Providing possibility of accessing objects as arrays
 * 
 * @author Sven Schrodt<sven@schrodt.club>
 * @link https://github.com/SchrodtSven/P8One
 * @package P8One
 * @version 0.1
 * @since 2023-04-25
 */



namespace SchrodtSven\P8\Internal;

trait ArrayAccessTrait
{
    


    public function offsetGet($offset): mixed
    {
        return $this->content[$offset] ?? null;
    }

    public function offsetSet($offset, $value): void
    {
        if (is_null($offset)) {
            $this->content[] = $value;
        } else {
            $this->content[$offset] = $value;
        }
    }

    public function offsetExists($offset): bool
    {
        return isset($this->content[$offset]);
    }

    public function offsetUnset($offset): void
    {
        unset($this->content[$offset]);
    }

}