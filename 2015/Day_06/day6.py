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
def parse(n):
    [z, x0, y0, x1, y1] = re.search('(\w+) (\d+),(\d+) through (\d+),(\d+)', n).groups()
    return z, slice(int(x0), int(x1) + 1), slice(int(y0), int(y1) + 1)


arr = np.zeros((1000, 1000), dtype=np.int)
for i in day.lines():
    a, b, c = parse(i)
    if a == 'toggle':
        arr[b, c] ^= 1
    else:
        arr[b, c] = ['off', 'on'].index(a)
day.part_one = sum(sum(arr))

arr = np.zeros((1000, 1000), dtype=np.int)
for i in day.lines():
    a, b, c = parse(i)
    arr[b, c] += {'off': -1, 'on': 1, 'toggle': 2}[a]
    arr[arr < 0] = 0
day.part_two = sum(sum(arr))

# ...and ends here
day.end = timer()
day.print()
