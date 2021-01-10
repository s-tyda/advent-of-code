from itertools import combinations
from math import prod
from aocdays import AoCDay
from timeit import default_timer as timer
from rich.console import Console
from rich.table import Table
from rich import print
from pathlib import Path

day = AoCDay(Path.cwd().parent.name, Path(__file__).name[3:-3])

# Solution 1 - creating reusable function
day.start = timer()


def execute(n):
    return next(prod(x) for x in combinations([int(x) for x in open(day.input)], n) if sum(x) == 2020)


day.part_one = execute(2)
day.part_two = execute(3)

day.end = timer()
day.print()

# Solution 2 - oneliners
# Method 1 - the fastest one
day.start = timer()

day.part_one = [x * y for (x, y) in combinations([int(x) for x in open(day.input)], 2) if x + y == 2020][0]
day.part_two = [x * y * z for (x, y, z) in combinations([int(x) for x in open(day.input)], 3) if x + y + z == 2020][0]

day.end = timer()
day.print(True)

# Method 2 - using prod() and sum(), slower
day.start = timer()

day.part_one = [prod(x) for x in combinations([int(x) for x in open(day.input)], 2) if sum(x) == 2020][0]
day.part_two = [prod(x) for x in combinations([int(x) for x in open(day.input)], 3) if sum(x) == 2020][0]

day.end = timer()
day.print(True)
