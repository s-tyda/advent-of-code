from itertools import combinations
from math import prod

# Solution 1 - prefer this for oneliners
# Part 1
print("Part 1: {}".format([x * y for (x, y) in combinations([int(x) for x in open('data.txt')], 2) if x + y == 2020][0]))
# Part 2
print("Part 2: {}".format([x * y * z for (x, y, z) in combinations([int(x) for x in open('data.txt')], 3) if x + y + z == 2020][0]))


# Solution 2 - creating reusable function
def execute(n):
    print("Part {}: {}".format(n-1, next(prod(x) for x in combinations([int(x) for x in open('data.txt')], n) if sum(x) == 2020)))


# Part 1
execute(2)
# Part 2
execute(3)
