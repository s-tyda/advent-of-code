from parse import *
x = {search('{} bag', x)[0]: [*findall('{:d} {} bag', x)] for x in open('data.txt')}


def f(c): return any(d == 'shiny gold' or f(d) for _, d in x[c])
def g(c): return sum(n + n * g(d) for n, d in x[c])


print(f"Part 1: {sum(map(f, x))}")
print(f"Part 2: {g('shiny gold')}")
