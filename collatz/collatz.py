#!/usr/bin/python

import argparse
import sys
import time
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

"""Python program to find the number of steps to reach 1 for the Collatz
   problem for user supplied value of n.
   A plot of sequence index versus sequence value is also created.
   For background on the Collatz Conjecture see:
   https://en.wikipedia.org/wiki/Collatz_conjecture
   Version 1.0
"""
# -------------------------------------------------------------------------
#
# Let N be the natural numbers, and N+ be the positive integers.
#
# Define f: N+ -> N as
# f(n) = { n/2      if n is even
#        { 3*n+1    if n is odd
#
# For n in N+, define sequence S: N -> N as
# S(i) = { n         if i = 0
#        { f(S(i-1)) if i > 0
#
# Hence S(i) is the value of f applied to n recursively i times.
# The smallest i such that S(i) = 1 is called the total stopping time of n.
# The Collatz conjecture is that such an i exists for every n.
# We define collatz(n) to be the smallest such i.
#
# In what follows we represent S as a python list. We stop listing values
# of S as soon as it takes the value 1, even though the above definition
# defines S on every natural number. So we have collatz(n) = len(S)-1 in
# python.
#
# f(1) = 4, f(2) = 1, f(3) = 10
# For n = 1 we have S = [1] and collatz(1) = 0.
# For n = 2 we have S = [2, 1] and collatz(2) = 1.
# For n = 3 we have S = [3, 10, 5, 16, 8, 4, 2, 1] and collatz(3) = 7.
# For n = 4 we have S = [4, 2, 1] and collatz(4) = 2
#
# Note also that in terms of the Kleene mu operator we have ...
# Let R = {i in N: S(i) = 1}.
# collatz(n) = (mu i) R(i).
# See: https://en.wikipedia.org/wiki/%CE%9C_operator
# 
# -------------------------------------------------------------------------

# Count the *total* number of recursive calls.
# Note: This is not the number of simultaneous frames on the call stack!
#       In fact, the way this is coded, the recursive function is at most
#       on the call stack collatz(n)+1 times at any one time. It takes
#       a very large number n to exceed the Python default recursive stack
#       maximum of 1000.
#       n = 670,617,279 has 986 steps, while
#       n = 9,780,657,630 has 1132 steps.
#       Hence, someplace between those two values the maximum will be
#       exceeded.
recursive_count = 0


def f_op(n):
    """The auxiliary function to be applied."""

    assert n > 0

    if n % 2 == 0:
        # n is even.
        return int(n/2)
    else:
        # n is odd.
        return 3 * n + 1


def s_seq_recursive(i, n, rec_stack_count):
    """The ith term of the Collatz sequence for positive integer n."""

    global recursive_count

    assert n > 0

    rec_stack_count += 1
    recursive_count += 1
    if i == 0:
        return n, rec_stack_count
    else:
        v, rec_stack_count = s_seq_recursive(i - 1, n, rec_stack_count)
        return f_op(v), rec_stack_count


def s_seq_iterative(i, n):
    """The ith term of the Collatz sequence for positive integer n."""

    assert n > 0

    value = n
    for _ in range(0, i):
        value = f_op(value)
    return value


def collatz_recursive(n):
    """Computes collatz(n) using recursion."""

    assert n > 0

    i = 0
    max_rec_stack = 0
    current_rec_stack = 0
    value, current_rec_stack = s_seq_recursive(i, n, current_rec_stack)
    max_rec_stack = max(max_rec_stack, current_rec_stack)
    while value != 1:
        i += 1
        current_rec_stack = 0
        value, current_rec_stack = s_seq_recursive(i, n, current_rec_stack)
        max_rec_stack = max(max_rec_stack, current_rec_stack)
    return i, max_rec_stack


def collatz_iterative(n):
    """Computes collatz(n) iteratively."""

    assert n > 0

    i = 0
    value = s_seq_iterative(i, n)
    while value != 1:
        i += 1
        value = s_seq_iterative(i, n)
    return i


def collatz_smart(n):
    """ Computes collatz(n) smartly.
        Also returns all the sequence values.
    """

    assert n > 0

    i = 0
    value = n
    sequence_of_values = [n]
    while value != 1:
        i += 1
        value = f_op(value)
        sequence_of_values.append(value)
    return i, sequence_of_values


# noinspection SpellCheckingInspection
def do_plotting(n, sequence_of_values):
    """Plot the values of the sequence for the Collatz n problem."""

    assert n > 0

    # Save the plot to a PDF file as well as displaying interactively.
    pdf_file = "collatz_plot_{}.pdf".format(n)
    print("Plot will be saved to file {}".format(pdf_file))
    with PdfPages(pdf_file) as pdf:
        # The sequence length is one more than the collatz value because
        # numpy starts counting at 1 instead of 0.
        sequence_length = len(sequence_of_values)
        # x values are [1, sequence_length]
        # Y values are the values in sequence_of_values
        x_values = np.linspace(1, sequence_length,
                               num=sequence_length, endpoint=True)
        y_values = np.array(sequence_of_values)
        plt.plot(x_values, y_values, color="blue", linewidth=2.5, linestyle="-")
        plt.xlim(0, x_values.max()*1.1)
        # plt.xticks()
        plt.ylim(0, y_values.max()*1.1)
        # plt.yticks()
        plt.xlabel("Sequence index")
        plt.ylabel("Sequence value")
        plt.title("Collatz Sequence {}".format(n), loc='center')
        pdf.savefig()
        plt.show()
        plt.close()


def run(n):
    """Run the program with arguments checked."""

    print("Computing collatz_smart({})".format(n))
    start_time = time.time()
    collatz, sequence_of_values = collatz_smart(n)
    end_time = time.time()
    print("The collatz of {}".format(n), "is {}".format(collatz))
    print("Execution time in secs was {}".format(end_time-start_time))
    print()

    print("Computing collatz_iterative({})".format(n))
    start_time = time.time()
    collatz = collatz_iterative(n)
    end_time = time.time()
    print("The collatz of {}".format(n), "is {}".format(collatz))
    print("Execution time in secs was {}".format(end_time-start_time))
    print()

    print("Computing collatz_recursive({})".format(n))
    start_time = time.time()
    try:
        collatz, rec_stack_count = collatz_recursive(n)
        print("The collatz of {}".format(n), "is {}".format(collatz))
        print("s_seq_recursive was on the stack a maximum of",
              "{} times.".format(rec_stack_count))
    except RecursionError:
        print("Too many recursive calls.")
        sys.exit(1)
    end_time = time.time()

    print("The number of recursive calls was {}".format(recursive_count))
    print("Execution time in secs was {}".format(end_time-start_time))

    do_plotting(n, sequence_of_values)


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

    if n <= 0:
        print('error: n must be greater than 0')
        sys.exit(1)

    recursion_limit = sys.getrecursionlimit()
    print("Note: The maximum recursion limit is by default",
          "{}\n".format(recursion_limit))
    # Use sys.setrecursionlimit(value) to change recursion limit.

    # NB: Despite the default recursion limit being 1000, we will not
    # exceed the default python recursion limit except for very large n.
    # n = 670,617,279 has 986 steps. Hence on the stack that many times +1.
    # n = 9,780,657,630 has 1132 steps.
    max_n = 670617279
    if n > max_n:
        print("error: n must be less than {}".format(max_n))
        sys.exit(1)


def run_with_args(args):
    """Run the program with args already parsed."""

    sanity_check_args(args.n)
    n = int(args.n)
    run(n)


def main():
    """Main collatz code with command line parser."""

    parser = argparse.ArgumentParser(description="Computes collatz(n)")
    parser.add_argument('n', type=int,
                        help='argument of collatz function')
    parser.set_defaults(func=run_with_args)
    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    # Call main() if run from command line.
    main()
