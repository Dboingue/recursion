#!/usr/bin/python

"""Create sample output file."""

import subprocess
import os

try:
    os.remove("sample_output.txt")
except OSError:
    pass

with open("sample_output.txt", 'a+') as sample:
    print(">python fib.py -h", file=sample, flush=True)
    subprocess.run(["python", "fib.py", "-h"],
                   shell=True,
                   stdout=sample,
                   stderr=subprocess.STDOUT)
    print(file=sample)

    print(">python fib.py a", file=sample, flush=True)
    subprocess.run(["python", "fib.py", "a"],
                   shell=True,
                   stdout=sample,
                   stderr=subprocess.STDOUT)
    print(file=sample)

    print(">python fib.py -1", file=sample, flush=True)
    subprocess.run(["python", "fib.py", "-1"],
                   shell=True,
                   stdout=sample,
                   stderr=subprocess.STDOUT)
    print(file=sample)

    print(">python fib.py 0", file=sample, flush=True)
    subprocess.run(["python", "fib.py", "0"],
                   shell=True,
                   stdout=sample,
                   stderr=subprocess.STDOUT)
    print(file=sample)

    print(">python fib.py 10", file=sample, flush=True)
    subprocess.run(["python", "fib.py", "10"],
                   shell=True,
                   stdout=sample,
                   stderr=subprocess.STDOUT)
    print(file=sample)

    print(">python fib.py 50", file=sample, flush=True)
    subprocess.run(["python", "fib.py", "50"],
                   shell=True,
                   stdout=sample,
                   stderr=subprocess.STDOUT)
    print(file=sample)

    print(">python fib.py 30", file=sample, flush=True)
    subprocess.run(["python", "fib.py", "30"],
                   shell=True,
                   stdout=sample,
                   stderr=subprocess.STDOUT)

    print(">python fib.py 31", file=sample, flush=True)
    subprocess.run(["python", "fib.py", "31"],
                   shell=True,
                   stdout=sample,
                   stderr=subprocess.STDOUT)
