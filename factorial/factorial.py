#!/usr/bin/python

"""Python program to find the factorial of a number provided by the user.
   Version 1.0
"""

import argparse
import sys
import time

# Count the number of recursive calls to the recursive function.
# This is not the count of function calls on the stack! That's because
# Python internal functions and other functions of this code could be
# on the stack when the recursive function is called.
recursive_count = 0


def factorial_recursive(n):
    """Computes factorial(n) using recursion.
        This will fail with n > 994 with the error
        RecursionError: maximum recursion depth exceeded in comparison
    """
    global recursive_count

    recursive_count += 1
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)


def factorial_iterative(n):
    """Computes factorial(n) iteratively."""

    factorial = 1
    if n == 0:
        pass
    else:
        for i in range(1, n + 1):
            factorial = factorial * i
    return factorial


def run(n):
    """Run the program with arguments checked."""

    print("Computing factorial_iterative({})".format(n))
    start_time = time.time()
    factorial = factorial_iterative(n)
    end_time = time.time()
    print("The factorial of {}".format(n), "is {}".format(factorial))
    print("Execution time in secs was {}".format(end_time-start_time))
    print()
    print("Computing factorial_recursive({})".format(n))
    start_time = time.time()
    try:
        factorial = factorial_recursive(n)
        print("The factorial of {}".format(n), "is {}".format(factorial))
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
    print("Note: The maximum recursion limit is by default",
          "{}\n".format(recursion_limit))
    # Use sys.setrecursionlimit(value) to change recursion limit.

    # NB: Despite the default recursion limit being 1000, doing 995
    # recursive calls causes an exception to be raised! Hence, the
    # limit for n is 994. It seems the reason for this is because
    # Python is counting everything on the stack; not just the recursive
    # function. Looking at the stack in the debugger when factorial_recursive
    # is first called, I see 4 other functions on the stack already;
    # factorial.py, main, run_with_args, and run.
    # So 1000 - 4 = 996. So once 995 calls are on the stack, we have
    # 999 calls on the stack and the next function added would bring the
    # total to 1000.
    max_n = 994
    if n > max_n:
        print("error: n must be less than {}".format(max_n))
        sys.exit(1)


def run_with_args(args):
    """Run the program with args already parsed."""

    sanity_check_args(args.n)
    n = int(args.n)
    run(n)


def main():
    """Main factorial code with command line parser."""

    parser = argparse.ArgumentParser(description="Computes factorial(n)")
    parser.add_argument('n', type=int,
                        help='argument of factorial function')
    parser.set_defaults(func=run_with_args)
    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    # Call main() if run from command line.
    main()
