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


# ...and ends here
day.end = timer()
day.print()
