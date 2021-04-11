#!/usr/bin/python

"""Create sample output file."""

import subprocess
import os

try:
    os.remove("sample_output.txt")
except OSError:
    pass

with open("sample_output.txt", 'a+') as sample:
    print(">python factorial.py -h", file=sample, flush=True)
    subprocess.run(["python", "factorial.py", "-h"],
                   shell=True,
                   stdout=sample,
                   stderr=subprocess.STDOUT)
    print(file=sample)

    print(">python factorial.py a", file=sample, flush=True)
    subprocess.run(["python", "factorial.py", "a"],
                   shell=True,
                   stdout=sample,
                   stderr=subprocess.STDOUT)
    print(file=sample)

    print(">python factorial.py -1", file=sample, flush=True)
    subprocess.run(["python", "factorial.py", "-1"],
                   shell=True,
                   stdout=sample,
                   stderr=subprocess.STDOUT)
    print(file=sample)

    print(">python factorial.py 0", file=sample, flush=True)
    subprocess.run(["python", "factorial.py", "0"],
                   shell=True,
                   stdout=sample,
                   stderr=subprocess.STDOUT)
    print(file=sample)

    print(">python factorial.py 10", file=sample, flush=True)
    subprocess.run(["python", "factorial.py", "10"],
                   shell=True,
                   stdout=sample,
                   stderr=subprocess.STDOUT)
    print(file=sample)

    print(">python factorial.py 100", file=sample, flush=True)
    subprocess.run(["python", "factorial.py", "100"],
                   shell=True,
                   stdout=sample,
                   stderr=subprocess.STDOUT)
    print(file=sample)

    print(">python factorial.py 1000", file=sample, flush=True)
    subprocess.run(["python", "factorial.py", "1000"],
                   shell=True,
                   stdout=sample,
                   stderr=subprocess.STDOUT)
