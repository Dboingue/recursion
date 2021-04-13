#!/usr/bin/python

"""Python program to create a binary tree with n nodes and print it.
   Version 1.0
"""

import argparse
import sys
import time
import statistics
import random

# Count the number of calls to the recursive print function.
# Note: This is not the number of simultaneous frames on the call stack!
recursive_print_count = 0


class Node:
    """An implementation of a binary tree."""

    # The indentation level for the print method.
    indent_level = 0

    def __init__(self, data):
        """Initialize a node."""

        self.data = data
        self.left = None
        self.right = None

    def print_data(self):
        """Print a tree's data in depth-first order."""

        if self.left:
            self.left.print_data()
            print(" ", end='')
        print(self.data, end='')
        if self.right:
            print(" ", end='')
            self.right.print_data()

    def print(self):
        """ Print a tree in preorder with indentation.
            None pointers printed as a dash "-".
        """
        global recursive_print_count

        recursive_print_count += 1
        if self.data >= 0:
            # Node has good data.
            print(" " * Node.indent_level, end='')
            print(self.data)
            Node.indent_level += 4
            if self.left is not None:
                self.left.print()
            else:
                print(" " * Node.indent_level, "-", sep='')
            if self.right is not None:
                self.right.print()
            else:
                print(" " * Node.indent_level, "-", sep='')
            Node.indent_level -= 4
        else:
            print("Node has bad data!")

    def insert(self, data):
        """ Insert data into tree.
            Recursively with smaller values to the left.
            Hence, recursive depth-first search has sorted data!
            Data is never entered more than once in the tree.
        """

        if self.data != data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)


def run(n, m, use_debug_problem=False):
    """ Create a binary tree with n nodes with random values from 0
        through m-1. If use_debug_problem is True then the m is ignored
        and the values are 0 through n-1.
    """

    start_time = time.time()

    if use_debug_problem:
        print("Creating a binary tree with {} nodes".format(n),
              "with values from 0 through {}".format(n-1))
        my_sample = list(range(0, n))
        if m > n:
            print("Maximum value {} ignored!".format(m))
    else:
        print("Creating a binary tree with {} nodes".format(n),
              "with values from 0 through {}".format(m-1))
        my_sample = random.sample(range(m), n)

    # To balance the tree we want the root's value to be the low median
    # of the sample. The low median is always a member of the list.
    my_low_median = statistics.median_low(my_sample)
    my_tree = Node(my_low_median)

    for i in my_sample:
        my_tree.insert(i)
    end_time = time.time()
    print("Execution time in secs was {}".format(end_time-start_time))
    print("The tree's data is ...")
    my_tree.print_data()
    print()
    print("The tree is ...")
    my_tree.print()
    print("There were {} calls to the".format(recursive_print_count),
          "recursive print method.")


def check_num(s):
    """Check that a string is an integer."""

    try:
        int(s)
        return True
    except ValueError:
        return False


# noinspection SpellCheckingInspection
def sanity_check_args(n, args):
    """Sanity check the user arguments."""

    if check_num(n):
        n = int(n)
        m = n
    else:
        print('error: {}'.format(n), ' is not a number.')
        sys.exit(1)

    if n <= 0:
        print('error: n must be greater than 0.')
        sys.exit(1)

    if args.max:
        if check_num(args.max):
            m = int(args.max)
        else:
            print('error: {}.format(args.max)', 'is not a number.')
            sys.exit(1)

    if m < n:
        print('error: max must be at least n = {}'.format(n))
        sys.exit(1)

    recursion_limit = sys.getrecursionlimit()
    print("Note: The maximum default recursion limit is",
          "{}\n".format(recursion_limit))
    # Use sys.setrecursionlimit(value) to change recursion limit.

    # NB: Despite the default recursion limit being 1000 we do not usual get
    # that many stack frames at once. The reason is that the tree was
    # balanced by putting the midpoint value at the root. The maximum
    # number of recursive calls would be determined by the height of the
    # tree. That height is >= log_2(n+1) - 1.
    max_n = 2000
    if n > max_n:
        print("error: n must be less than {}".format(max_n))
        sys.exit(1)


def run_with_args(args):
    """Run the program with args already parsed."""

    sanity_check_args(args.n, args)
    n = int(args.n)
    m = n
    if args.max:
        m = int(args.max)
    use_debug_problem = False
    if args.use_debug_problem:
        use_debug_problem = True
    run(n, m, use_debug_problem=use_debug_problem)


def main():
    """Main code with command line parser."""

    parser = argparse.ArgumentParser(
            description="Creates a binary tree with n nodes with values "
                        + "0 through n-1. "
                        + "If max is specified then n values are chosen "
                        + "randomly between 0 and max-1 inclusive.")
    parser.add_argument('n', type=int,
                        help="number of nodes")
    parser.add_argument('--max', type=int,
                        help="maximum value for nodes")
    parser.add_argument('--use_debug_problem', action='store_true',
                        help="use a special problem for debugging")
    parser.set_defaults(func=run_with_args)
    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    # Call main() if run from command line.
    main()
