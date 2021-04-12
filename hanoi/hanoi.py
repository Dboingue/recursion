#!/usr/bin/python

import argparse
import sys

"""Towers of Hanoi Puzzle
   Version 1.0
"""

# The Towers of Hanoi Puzzle
#
# We are given a wooden board from which three posts project. On the left
# post is a stack of graduated disks such that the bottom one has the largest
# diameter and no larger disk rests on a smaller one.  
#
#     |          |          |         
#    -|-         |          |         
#   --|--        |          |         
#  ---|---       |          |         
# ----|----      |          |         
# ===============================
#
# The problem is to devise an algorithm for moving n disks from the left post
# to the right post observing the two following rules.
#
# (a) Only one disk can be moved at a time.
# (b) No disk is ever to rest on a smaller one.
#
# [It is implied that when a disk is moved it is moved to one of the posts;
#  otherwise a solution would be to move all the disks off the first post
#  onto a table and then re-stack them on the third post!]
#
# The algorithm should print out some kind of directions that a person can
# follow to carry out the actions required to move the disks.
#
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# Global Constants.
# The maximum number of disks.
# Set to something reasonable!
_MAX_DISKS = 15
# The maximum number of posts. (The number of posts is set to the maximum
# and is assumed to be 3.)
_MAX_POSTS = 3

# ----------------------------------------------------------------------
# Global Variables.

# The number of disks we have.
number_of_disks = _MAX_DISKS

# The disks are numbered 1, 2, ..., number_of_disks such that the larger disks
# have the larger numbers. So the largest disk is numbered number_of_disks etc.
#
# The post are numbered 1, 2, ..., _MAX_POSTS. The numbering is from left
# to right so that the left most post is numbered 1.
#
# disk_at_position[i][j] is the number of the disk on post i at location j,
# where the bottom most location is numbered 0 and the top is
# number_of_disks-1.
# If no disk is at the location, then the value is 0.
# Will be initialized as ...
# disk_at_position = [[0 for _ in range(0, number_of_disks)]
#                     for _ in range(0, _MAX_POSTS+1)]
disk_at_position = []

# The location of the top disk on each post.
# If no disks are on the post then this will be set to -1.
top_disk_location = [-1] * (_MAX_POSTS + 1)

# Let us keep track of how many moves it takes.
# It should take 2^n - 1 moves.
number_of_moves = 0

# Count the number of calls to the recursive function.
# Note: This may not be the number of simultaneous frames on the call stack!
#       In fact, the way this is coded, the recursive function is at most
#       on the call stack number_of_disks-1 times at any one time.
recursive_count = 0

# Hence, for 4 disks we have...
#                                    Levels are [-1, number_of_disks]
#     |          |          |        4             Disk
#    -|-         |          |        3             1
#   --|--        |          |        2             2
#  ---|---       |          |        1             3
# ----|----      |          |        0             4
# ===============================   -1
#     1          2          3      <-Post numbers [1, _MAX_POSTS]
#
# Note the display size of the disk including the post is disk_number*2 + 1.
# The various variables for the above diagram would be...
# number_of_disks = 4                     d[post][location]
# disk_at_position = [[0, 0, 0, 0],       d[0][0] ... d[0][3]   unused!
#                     [4, 3, 2, 1],       d[1][0] ... d[1][3]
#                     [0, 0, 0, 0],       d[2][0] ... d[2][3]
#                     [0, 0, 0, 0]]       d[3][0] ... d[3][3]
# top_disk_location = [-1, 3, -1, -1]
# Note the way you have to "turn your head" to make disk_at_position
# look like the locations in the picture. The same thing happened in
# my n-Queen program. The arrays are like a math matrix (zero-based)
# where counting is top-down, but we count in the picture from the bottom.

# ----------------------------------------------------------------------
# Local functions.


def print_between_post(level):
    """ Print the correct character between what has been printed
        and the printing for the next post - enough times to make
        some space between the disks/posts at the given 'level'.
    """

    # Character to print between the post.
    char_to_print = ' '

    # Special case of the base of the puzzle.
    if level == -1:
        char_to_print = '='

    # The way this is done there is at least one character printed
    # (cases of number_of_disks 1, 2, 3) and then (4,5) -> 2
    # (6,7) -> 3, (8,9) -> 4, etc.
    for i in range(0, int(number_of_disks/2)):
        print(char_to_print, end='')


def print_location(post, level):
    """Print the correct character for the given post and location."""

    # Normal characters used to print the puzzle.
    disk_char = '-'
    empty_char = ' '
    post_char = '|'

    # Exceptions for first and last lines.
    if level == number_of_disks:
        # First line has no disks.
        disk_char = ' '
        empty_char = ' '
        post_char = '|'
    elif level == -1:
        # Last line is the base of the puzzle.
        disk_char = '='
        empty_char = '='
        post_char = '='

    # Break up the location printing into 5 parts.
    # Left and right of the post, in or out of the disk, and the post itself.
    # If L is the length of the print area, C the center index of that area,
    # l the index of the left side of the disk and r the index of the right
    # side of the disk, then the 5 parts are the intervals:
    # [1,l), [l,C), [C,C], (C,r], (r,L]. Note that if there is no disk, then
    # l=r=C and the second and fourth intervals are null.
    # We also want to print space between the posts.
    # For 4 disks we have...
    #                                    Levels  [-1, number_of_disks]
    #     |          |          |        4             Disk
    #    -|-         |          |        3             1
    #   --|--        |          |        2             2
    #  ---|---       |          |        1             3
    # ----|----      |          |        0             4
    # ===============================   -1
    #     1          2          3      <-Post numbers [1, _MAX_POSTS]
    #
    # So for 4 total disks we have L = 9 and for disk 2 ...
    #   --|--        |          |
    #   l C r
    # 123456789**123456789**123456789
    # With int(number_of_disks/2) spaces between; i.e. the "*".

    disk_number = 0
    if (level >= 0) and (level < number_of_disks):
        disk_number = disk_at_position[post][level]

    length = number_of_disks*2 + 1
    center = number_of_disks + 1
    left_side = center - disk_number
    right_side = center + disk_number

    for i in range(1, left_side):
        print(empty_char, end='')
    for i in range(left_side, center):
        print(disk_char, end='')
    print(post_char, end='')

    for i in range(center+1, right_side+1):
        print(disk_char, end='')
    for i in range(right_side+1, length+1):
        print(empty_char, end='')


def print_puzzle():
    """Print the puzzle."""

    for k in reversed(range(-1, number_of_disks+1)):
        for j in range(1, _MAX_POSTS+1):
            print_location(j, k)
            if j != _MAX_POSTS:
                print_between_post(k)
        print()


def initialize_stack(start_post, size):
    """ Initialize the stack of disks.
        Put the number of disks given in 'size' on the post given in
        'start_post'.
    """

    global disk_at_position
    global top_disk_location

    assert(start_post >= 1) and (start_post <= _MAX_POSTS)
    assert(size >= 1) and (size <= _MAX_DISKS)

    # Zero out the entire array of disks positions.
    disk_at_position = [[0 for _ in range(0, size)]
                        for _ in range(0, _MAX_POSTS+1)]

    # Also set the top locations to show no disks on the posts.
    top_disk_location = [-1] * (_MAX_POSTS+1)

    # Put the disks on the start_post post.
    # The largest disk goes on first.
    j = 0
    for i in reversed(range(1, size+1)):
        disk_at_position[start_post][j] = i
        # Prepare next location.
        j += 1

    # Set the top disk location.
    top_disk_location[start_post] = size - 1


def move_disk(start_post, end_post):
    """Move a single disk from post 'start_post' to post 'end_post'."""

    global number_of_moves

    assert(start_post >= 1) and (start_post <= _MAX_POSTS)
    assert(end_post >= 1) and (end_post <= _MAX_POSTS)

    location_on_start_post = top_disk_location[start_post]
    assert(location_on_start_post >= 0) and\
          (location_on_start_post < _MAX_DISKS)

    location_on_end_post = top_disk_location[end_post]
    assert(location_on_end_post >= -1) and (location_on_end_post < _MAX_DISKS)

    new_location_on_end_post = location_on_end_post + 1
    disk_on_start_post = disk_at_position[start_post][location_on_start_post]

    # Say what to do.
    number_of_moves += 1
    if location_on_end_post >= 0:
        disk_on_end_post = disk_at_position[end_post][location_on_end_post]
        print("Move disk number {} on top".format(disk_on_start_post),
              "on post {}".format(start_post),
              "on top disk number {}".format(disk_on_end_post),
              "on post {}.".format(end_post))
    else:
        print("Move disk number {}".format(disk_on_start_post),
              "on post {}".format(start_post),
              "to post number {}".format(end_post))

    # Move the disk.
    disk_at_position[end_post][new_location_on_end_post] = disk_on_start_post
    top_disk_location[end_post] = new_location_on_end_post
    disk_at_position[start_post][location_on_start_post] = 0
    top_disk_location[start_post] -= 1
    print_puzzle()


def transfer_stack(start_post, end_post, intermediate_post, size):
    """ Transfer the stack of disks on post 'start_post' to post
        'end_post' using post 'intermediate_post'.
        The number of disks to move is given by 'size'.
     """
    global recursive_count

    recursive_count += 1
    if size == 1:
        move_disk(start_post, end_post)
    else:
        transfer_stack(start_post, intermediate_post, end_post, size-1)
        move_disk(start_post, end_post)
        transfer_stack(intermediate_post, end_post, start_post, size-1)


def run(n):
    """Solves the Tower of Hanoi puzzle for n disks."""
    global number_of_disks

    number_of_disks = n
    start_post = 1
    end_post = 3
    intermediate_post = 2

    initialize_stack(start_post, number_of_disks)
    print_puzzle()
    transfer_stack(start_post, end_post, intermediate_post, number_of_disks)
    print("It took {} moves.".format(number_of_moves))
    print("The number of recursive calls was {}".format(recursive_count))


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

    if n > _MAX_DISKS:
        print("error: n must be less than {}.".format(_MAX_DISKS+1))
        sys.exit(1)

    recursion_limit = sys.getrecursionlimit()
    print("Note: The maximum default recursion limit is",
          "{}\n".format(recursion_limit))
    # Use sys.setrecursionlimit(value) to change recursion limit.

    # NB: Despite the default recursion limit being 1000, we may
    # not be able to do that many. Debugger inspection shows that
    # when transfer_stack is first called there are already 4 function calls
    # on the stack. Hence, with a default limit by Python of 1000, we
    # can only do 994. Of course that is a ridiculous number of disks because
    # the answer will take too long to print anyway! Hence, let's set the
    # limit to something reasonable.
    max_n = _MAX_DISKS
    if n > max_n:
        print("error: n must be less than {}".format(max_n))
        sys.exit(1)


def run_with_args(args):
    """Run the program with args already parsed."""

    sanity_check_args(args.n)
    n = int(args.n)
    run(n)


def main():
    """Main hanoi code with command line parser."""
    parser = argparse.ArgumentParser(
        description="Solves Tower of Hanoi for n disks.")
    parser.add_argument('n', type=int,
                        help='number of disks')
    parser.set_defaults(func=run_with_args)
    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    # Call main() if run from command line.
    main()
