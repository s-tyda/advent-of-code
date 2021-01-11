import operator as op
import numpy as np
import re
import time
import itertools
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
import hashlib
day = AoCDay(Path.cwd().parent.name, Path(__file__).name[3:-3])
day.start = timer()

# Your code starts here...
code = day.lines()[0]
one, two = False, False
for i in itertools.count():
    hash_out = hashlib.md5(f"{code}{i}".encode()).hexdigest()
    if not two and hash_out.startswith("000000"):
        day.part_two = i
        two = True
    if not one and hash_out.startswith("00000"):
        day.part_one = i
        one = True
    if one and two:
        break
# ...and ends here
day.end = timer()
day.print()
