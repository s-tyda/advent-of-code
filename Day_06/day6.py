# Part 1
print("Part 1: {}".format(sum(len(set(i.replace('\n', ''))) for i in open('data.txt').read().split('\n\n'))))
# Part 2
print("Part 2: {}".format(sum(len(set.intersection(*[set(t) for t in i.split("\n")])) for i in open('data.txt').read().split("\n\n"))))
