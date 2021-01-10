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

# Simple solution
day.start = timer()

sum_one = 0
sum_two = 0
for i in day.lines():
    l, w, h = [int(x) for x in i.strip().split("x")]
    sum_one += 2 * l * w + 2 * l * h + 2 * w * h + min(l * w, l * h, w * h)
    sum_two += l * w * h + 2 * min(l + w, l + h, w + h)

day.part_one = sum_one
day.part_two = sum_two

day.end = timer()
day.print()

# One-liners
day.start = timer()

day.part_one = sum([2 * l * w + 2 * l * h + 2 * w * h + min(l * w, l * h, w * h) for l, w, h in [[int(x) for x in i.strip().split("x")] for i in day.lines()]])
day.part_two = sum([l * w * h + 2 * min(l + w, l + h, w + h) for l, w, h in [[int(x) for x in i.strip().split("x")] for i in day.lines()]])

day.end = timer()
day.print(True)
