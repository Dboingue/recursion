#!/usr/bin/python

"""Create sample output file."""

import subprocess
import os

try:
    os.remove("sample_output.txt")
except OSError:
    pass

with open("sample_output.txt", 'a+') as sample:
    print(">python collatz.py -h", file=sample, flush=True)
    subprocess.run(["python", "collatz.py", "-h"],
                   shell=True,
                   stdout=sample,
                   stderr=subprocess.STDOUT)
    print(file=sample)

    print(">python collatz.py a", file=sample, flush=True)
    subprocess.run(["python", "collatz.py", "a"],
                   shell=True,
                   stdout=sample,
                   stderr=subprocess.STDOUT)
    print(file=sample)

    print(">python collatz.py -1", file=sample, flush=True)
    subprocess.run(["python", "collatz.py", "-1"],
                   shell=True,
                   stdout=sample,
                   stderr=subprocess.STDOUT)
    print(file=sample)

    print(">python collatz.py 0", file=sample, flush=True)
    subprocess.run(["python", "collatz.py", "0"],
                   shell=True,
                   stdout=sample,
                   stderr=subprocess.STDOUT)
    print(file=sample)

    print(">python collatz.py 16", file=sample, flush=True)
    subprocess.run(["python", "collatz.py", "16"],
                   shell=True,
                   stdout=sample,
                   stderr=subprocess.STDOUT)
    print(file=sample)

    print(">python collatz.py 27", file=sample, flush=True)
    subprocess.run(["python", "collatz.py", "27"],
                   shell=True,
                   stdout=sample,
                   stderr=subprocess.STDOUT)
    print(file=sample)

    print(">python collatz.py 670617279", file=sample, flush=True)
    subprocess.run(["python", "collatz.py", "670617279"],
                   shell=True,
                   stdout=sample,
                   stderr=subprocess.STDOUT)
    print(file=sample)

    print(">python collatz.py 670617280", file=sample, flush=True)
    subprocess.run(["python", "collatz.py", "670617280"],
                   shell=True,
                   stdout=sample,
                   stderr=subprocess.STDOUT)
