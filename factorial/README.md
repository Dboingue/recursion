This is the usual function one sees given as a first example of a recursively defined function. That is, a function defined in terms of itself.

See:
* Recursion
https://en.wikipedia.org/wiki/Recursion
* Factorial
https://en.wikipedia.org/wiki/Factorial

Note that there are multiple definitions for "function" as well as for "recursion". The context usually makes it clear which definition is intended.

While factorial(n) may first be thought of as the product of all positive integers less than or equal to n, it is useful to have factorial(0) defined. The reasons are well explained on the Wikipedia link above. Hence, with N being the natural numbers, and N+ being the positive integers, we have factorial:N -> N+ defined recursively as
factorial(0) = 1 and for n > 0, factorial(n) = n* factorial(n-1). That is, the domain of factorial is N, and its codomain is N+.

The factorial function grows very fast; faster than all polynomials and exponential functions. Hence, for large n, computing factorial(n) on a computer can be an issue. In some computer languages one would quickly exceed the maximum value allowed for the return type; say an "int". In Python, when the value gets large, Python changes the type to allow very large positive integers. However, at some value of n, one will exceed the capabilities of the machine!




