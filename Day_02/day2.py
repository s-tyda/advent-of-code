from functools import reduce
# Part 1
print("Part 1: {}".format(sum([1 if int(i[0].split("-")[0]) <= i[2].count(i[1][0]) <= int(i[0].split("-")[1]) else 0 for i in [x.split() for x in open('data.txt')]])))
# Part 2
print("Part 2: {}".format(sum([reduce(lambda d, e: d ^ e, [i[2][int(x) - 1] == i[1][0] for x in i[0].split('-')])for i in [x.split() for x in open('data.txt')]])))
