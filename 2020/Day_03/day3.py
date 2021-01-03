from math import prod
# Part 1
print("Part 1: {}".format(sum([line[(3 * i) % len(line)] == '#' for i, line in enumerate([x.strip('\n') for x in open("data.txt")][::1])])))
# Part 2
print("Part 2: {}".format(prod([sum([line[(dx * i) % len(line)] == '#' for i, line in enumerate([x.strip('\n') for x in open("data.txt")][::dy])]) for dx, dy in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]])))
