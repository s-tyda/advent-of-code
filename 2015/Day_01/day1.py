import operator as op
import numpy as np
import re
import time
from itertools import combinations, product, chain
from functools import reduce, lru_cache
from collections import deque, Counter
from toolz import partition
from math import prod
from array import array
from parse import *
from timeit import default_timer as timer
from aocdays import AoCDay
from pathlib import Path

day = AoCDay(Path.cwd().parent.name, Path(__file__).name[3:-3])

# Simple, fast solution
day.start = timer()

sum = 0
got = False
for idx, i in enumerate(day.lines()[0]):
    if i == '(':
        sum += 1
    elif i == ')':
        sum -= 1
    if not got and sum == -1:
        got = idx + 1

day.part_one = sum
day.part_two = got

day.end = timer()
day.print()

# One-liners
day.start = timer()

day.part_one = eval(f"0+{day.lines()[0].translate(str.maketrans({'(': '+1', ')': '-1'}))}")
day.part_two = (lambda line: [i for i in range(len(line)) if line[:i].count("(") - line[:i].count(")") == -1][0])(day.lines()[0])

day.end = timer()
day.print(True)
