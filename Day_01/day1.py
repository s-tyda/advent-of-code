from itertools import combinations
from math import prod

# Solution 1 - prefer this for oneliners
# Part 1
print([x * y for (x, y) in combinations([int(x) for x in open('data.txt').readlines()], 2) if x + y == 2020])
# Part 2
print([x * y * z for (x, y, z) in combinations([int(x) for x in open('data.txt').readlines()], 3) if x + y + z == 2020])


# Solution 2 - creating reusable function
def execute(n):
    print(next(prod(x) for x in combinations([int(x) for x in open('data.txt').readlines()], n) if sum(x) == 2020))


# Part 1
execute(2)
# Part 2
execute(3)
