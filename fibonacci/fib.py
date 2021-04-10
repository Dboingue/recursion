#!/usr/bin/python

"""Python program to find the nth Fibonacci number; n provided by the user.
    fib(0) = 0 , fib(1) = 1, fib(n) = fib(n-1) + fib(n-2) for n > 1.
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, ...
    Per: https://en.wikipedia.org/wiki/Fibonacci_number
   Version 1.0
"""

import argparse
import sys
import time

# Count the number of calls to the recursive function.
# Note: This is not the number of simultaneous frames on the call stack!
recursive_count = 0


def fib_recursive(n):
    """Computes fib(n) using recursion.
       While there are never more than n call frames to this function on
       the stack at any one time, this is an incredibly inefficient way
       to compute this function. For n=30, the function is called
       2,692,537 times!!
    """
    global recursive_count

    recursive_count += 1
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n):
    """Computes fib(n) iteratively."""

    if n == 0:
        return 0
    if n == 1:
        return 1

    fib_m2 = 0
    fib_m1 = 1
    fib = 0
    for i in range(1, n):
        fib = fib_m1 + fib_m2
        fib_m2 = fib_m1
        fib_m1 = fib
    return fib


def run(n):
    """Run the program with arguments checked."""

    print("Computing fib_iterative({})".format(n))
    start_time = time.time()
    fib = fib_iterative(n)
    end_time = time.time()
    print("The fib of {}".format(n), "is {}".format(fib))
    print("Execution time in secs was {}".format(end_time-start_time))
    print()
    print("Computing fib_recursive({})".format(n))
    start_time = time.time()
    try:
        fib = fib_recursive(n)
        print("The fib of {}".format(n), "is {}".format(fib))
    except RecursionError:
        print("Too many recursive calls.")
    end_time = time.time()
    print("The number of recursive calls was {}".format(recursive_count))
    print("Execution time in secs was {}".format(end_time-start_time))


def check_num(s):
    """Check that a string is an integer."""

    try:
        int(s)
        return True
    except ValueError:
        return False


# noinspection SpellCheckingInspection
def sanity_check_args(n):
    """Sanity check the user arguments."""

    if check_num(n):
        n = int(n)
    else:
        print('error: {}'.format(n), ' is not a number.')
        sys.exit(1)

    if n < 0:
        print('error: n must be greater than or equal to 0')
        sys.exit(1)

    recursion_limit = sys.getrecursionlimit()
    print("Note: The maximum recursion limit is {}\n".format(recursion_limit))
    # Use sys.setrecursionlimit(value) to change recursion limit.

    # NB: Dispite the default recursion limit being 1000, we may
    # not be able to do that many. However, for fib() it does not matter
    # because we will never get near the limit.
    # TODO: Warn about big n!
    max_n = 999
    if n > max_n:
        print("error: n must be less than {}".format(max_n))
        sys.exit(1)


def run_with_args(args):
    """Run the program with args already parsed."""

    sanity_check_args(args.n)
    n = int(args.n)
    run(n)


def main():
    """Main fib code with command line parser."""

    parser = argparse.ArgumentParser(description="Computes fib(n)")
    parser.add_argument('n', type=int,
                        help='argument of fib function')
    parser.set_defaults(func=run_with_args)
    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    # Call main() if run from command line.
    main()
