<h1>The Fibonacci Function</h1>
By the Fibonacci Function, I mean that function defined on the natural numbers, N, whose value at n is the nth value of the Fibonacci sequence as defined on the following Wikipedia page.

* Fibonacci Function:
https://en.wikipedia.org/wiki/Fibonacci_number

Each number in that sequence is the sum of the two preceding ones, starting from 0 and 1. Hence, using a recursive definition, we have

fib:N -> N+, with fib(0) = 0, fib(1) = 1, and for n > 1, fib(n) = fib(n-1) + fib(n-2)

The run time behavior of fib_recursive() is an excellent example of why one should be careful to not naively implement a function from its recursive definition. While there are never more than n call frames to this function on the call stack at any one time, this is an incredibly inefficient way to compute this function. For n=30, the function is called 2,692,537 times!! fib_interative() shows an implementation with a simple for-loop that has O(n) performance. There is a way to program this function and get O(1) performance! Look at the Wikipedia page for the formula.

<h2>Usage</h2>

````
usage: fib.py [-h] n

Computes fib(n)

positional arguments:
  n            argument of fib function

optional arguments:
  -h, --help   show this help message and exit
````
