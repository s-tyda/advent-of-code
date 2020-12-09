from parse import *
# Part 1
print(f"Part 1: {sum(map(f := lambda c: any(d == 'shiny gold' or f(d) for _, d in x[c]), x := {search('{} bag', x)[0]: [*findall('{:d} {} bag', x)] for x in open('data.txt')}))}")
# Part 2
print(f"Part 2: {(g := lambda c: sum(n + n * g(d) for n, d in x[c]))('shiny gold')}")
