# Day 6 Part 1
print(sum(len(set(i.replace('\n', ''))) for i in open('data.txt').read().split('\n\n')))
# Day 6 Part 2
print(sum(len(set.intersection(*[set(t) for t in i.split("\n")])) for i in open('data.txt').read().split("\n\n")))
