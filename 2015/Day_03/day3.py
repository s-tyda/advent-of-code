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
day.start = timer()

# Your code starts here...
signs = day.lines()[0]
houses = {(0, 0)}
i = 0
j = 0
for sign in signs:
    if sign == "^":
        i += 1
    elif sign == 'v':
        i -= 1
    elif sign == '<':
        j -= 1
    elif sign == '>':
        j += 1
    houses.add((i, j))
day.part_one = len(houses)

houses = {(0, 0)}
i = 0
j = 0
ii = 0
jj = 0
for idx, sign in enumerate(signs):
    if sign == "^":
        if idx % 2 == 0:
            i += 1
        else:
            ii += 1
    elif sign == 'v':
        if idx % 2 == 0:
            i -= 1
        else:
            ii -= 1
    elif sign == '<':
        if idx % 2 == 0:
            j -= 1
        else:
            jj -= 1
    elif sign == '>':
        if idx % 2 == 0:
            j += 1
        else:
            jj += 1
    if idx % 2 == 0:
        houses.add((i, j))
    else:
        houses.add((ii, jj))
day.part_two = len(houses)
# ...and ends here
day.end = timer()
day.print()
