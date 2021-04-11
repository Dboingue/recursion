#!/usr/bin/python

"""Create sample output file."""

import subprocess
import os

try:
    os.remove("sample_output.txt")
except OSError:
    pass

with open("sample_output.txt", 'a+') as sample:
    print(">python hanoi.py -h", file=sample, flush=True)
    subprocess.run(["python", "hanoi.py", "-h"],
                   shell=True,
                   stdout=sample,
                   stderr=subprocess.STDOUT)
    print(file=sample)

    print(">python hanoi.py a", file=sample, flush=True)
    subprocess.run(["python", "hanoi.py", "a"],
                   shell=True,
                   stdout=sample,
                   stderr=subprocess.STDOUT)
    print(file=sample)

    print(">python hanoi.py -1", file=sample, flush=True)
    subprocess.run(["python", "hanoi.py", "-1"],
                   shell=True,
                   stdout=sample,
                   stderr=subprocess.STDOUT)
    print(file=sample)

    print(">python hanoi.py 0", file=sample, flush=True)
    subprocess.run(["python", "hanoi.py", "0"],
                   shell=True,
                   stdout=sample,
                   stderr=subprocess.STDOUT)
    print(file=sample)

    print(">python hanoi.py 20", file=sample, flush=True)
    subprocess.run(["python", "hanoi.py", "20"],
                   shell=True,
                   stdout=sample,
                   stderr=subprocess.STDOUT)
    print(file=sample)

    print(">python hanoi.py 5", file=sample, flush=True)
    subprocess.run(["python", "hanoi.py", "5"],
                   shell=True,
                   stdout=sample,
                   stderr=subprocess.STDOUT)
    print(file=sample)

    print(">python hanoi.py 10", file=sample, flush=True)
    subprocess.run(["python", "hanoi.py", "10"],
                   shell=True,
                   stdout=sample,
                   stderr=subprocess.STDOUT)
