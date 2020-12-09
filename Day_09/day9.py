from itertools import combinations

with open('data.txt', 'r') as f:
    input = list(map(int, f.readlines()))

# Part 1
for i in range(25, len(input)):
    if input[i] not in [i + j for i, j in combinations(input[i - 25:i], 2)]:
        invalid = input[i]
        break
print(f'Part 1: {invalid}')

# Part 2
i = 0
j = 1
s = input[i]
while s != invalid:
    s += input[j]
    while s > invalid:
        s -= input[i]
        i += 1
    j += 1

print(f'Part 2: {min(input[i:j]) + max(input[i:j])}')
