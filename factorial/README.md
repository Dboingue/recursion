<h1>The Factorial Function and Recursion</h1>
This is the usual function one sees given as a first example of a recursively defined function. That is, a function defined in terms of itself.

See:
* Recursion
https://en.wikipedia.org/wiki/Recursion
* Factorial
https://en.wikipedia.org/wiki/Factorial

Note that there are multiple definitions for "function" as well as for "recursion". The context usually makes it clear which definition is intended.

While factorial(n) may first be thought of as the product of all positive integers less than or equal to n, it is useful to have factorial(0) defined. The reasons are well explained on the Wikipedia link above. Hence, with N being the natural numbers, and N+ being the positive integers, we have factorial:N -> N+ defined recursively as
factorial(0) = 1 and for n > 0, factorial(n) = n* factorial(n-1). That is, the domain of factorial is N, and its codomain is N+.

<h2>Usage</h2>

````
usage: factorial.py [-h] n

Computes factorial(n)

positional arguments:
  n           argument of factorial function

optional arguments:
  -h, --help  show this help message and exit
````

<h2>Computer Limitations</h2>
Computer limitations cause a few issues with programming the factorial function.

<h3>Variable Type Size Limits</h3>
The factorial function grows very fast; faster than all polynomials and exponential functions. Hence, for large n, computing factorial(n) on a computer can be an issue. In some computer languages one would quickly exceed the maximum value allowed for the return type; say an "int". In Python, when the value gets large, Python changes the type to allow very large positive integers. However, at some value of n, one will exceed the capabilities of the machine! However, there is another issue with computer language environments; the call stack.

<h3>The Call Stack</h3>
Every time a computer program calls a function (subroutine), it creates a call frame. That call frame contains the current execution pointer, and all the local variables and their values. The call frame is put in a call stack. When the code finally "returns" from the called function, the call frame is "popped" and the environment is reset to start execution where it left off, with all the local variables reinstated.
Different languages and programming environments handle the maximum size the call stack can be in different ways. Some have a default size that can be changed at compile time. Python has a default stack size of 1,000 that can be changed at any time the program is running by calling a special Python function. The limit of the call stack size is to help the programmer to not accidentally create a program that gets in an infinite loop.

In my program, before factorial_recursive() is called, there are already a few function calls on the stack. Hence, I made the maximum value of n be 994 to avoid what Python refers to as a "RecursionError" exception.

<h3>Tail Call Elimination</h3>
The factorial_recursive() impementation is a special kind of recursion called "tail recursion". Many compilers will optimize such a recursive call by eliminating the recursive call with essentially a goto statement. However, Python does not do tail call elimination; and it probably never will!

See:
* Tail call.
https://en.wikipedia.org/wiki/Tail_call
* Why Python does not do tail call elimination by Guido van Rossum; the inventor of the Python language.
http://neopythonic.blogspot.com/2009/04/tail-recursion-elimination.html

