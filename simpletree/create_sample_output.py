#!/usr/bin/python

"""Create sample output file."""

import subprocess
import os

try:
    os.remove("sample_output.txt")
except OSError:
    pass

with open("sample_output.txt", 'a+') as sample:
    print(">python simpletree.py -h", file=sample, flush=True)
    subprocess.run(["python", "simpletree.py", "-h"],
                   shell=True,
                   stdout=sample,
                   stderr=subprocess.STDOUT)
    print(file=sample)

    print(">python simpletree.py a", file=sample, flush=True)
    subprocess.run(["python", "simpletree.py", "a"],
                   shell=True,
                   stdout=sample,
                   stderr=subprocess.STDOUT)
    print(file=sample)

    print(">python simpletree.py -1", file=sample, flush=True)
    subprocess.run(["python", "simpletree.py", "-1"],
                   shell=True,
                   stdout=sample,
                   stderr=subprocess.STDOUT)
    print(file=sample)

    print(">python simpletree.py 0", file=sample, flush=True)
    subprocess.run(["python", "simpletree.py", "0"],
                   shell=True,
                   stdout=sample,
                   stderr=subprocess.STDOUT)
    print(file=sample)

    print(">python simpletree.py --max 20 30", file=sample, flush=True)
    subprocess.run(["python", "simpletree.py", "--max", "20", "30"],
                   shell=True,
                   stdout=sample,
                   stderr=subprocess.STDOUT)
    print(file=sample)

    print(">python simpletree.py 1", file=sample, flush=True)
    subprocess.run(["python", "simpletree.py", "1"],
                   shell=True,
                   stdout=sample,
                   stderr=subprocess.STDOUT)
    print(file=sample)

    print(">python simpletree.py 5", file=sample, flush=True)
    subprocess.run(["python", "simpletree.py", "--use_debug_problem", "5"],
                   shell=True,
                   stdout=sample,
                   stderr=subprocess.STDOUT)
    print(file=sample)

    print(">python simpletree.py --max 30 10", file=sample, flush=True)
    subprocess.run(["python", "simpletree.py", "--max", "30", "10"],
                   shell=True,
                   stdout=sample,
                   stderr=subprocess.STDOUT)
    print(file=sample)

    print(">python simpletree.py --max 100 20", file=sample, flush=True)
    subprocess.run(["python", "simpletree.py", "--max", "100", "20"],
                   shell=True,
                   stdout=sample,
                   stderr=subprocess.STDOUT)
