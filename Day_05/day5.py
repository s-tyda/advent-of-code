# Part 1
print("Part 1: {}".format(max(set(int(x.translate(str.maketrans("FBLR", "0101")), 2) for x in open('data.txt')))))
# Part 2
print("Part 2: {}".format((lambda s: next(i for i in range(min(s) + 1, max(s)) if i not in s))(set(int(x.translate(str.maketrans("FBLR", "0101")), 2) for x in open('data.txt')))))
