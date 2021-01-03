from collections import Counter
# Part 1
print("Part 1: {}".format((lambda counter: counter[1] * (counter[3] + 1))((lambda input: Counter(b - a for a, b in zip([0] + input, input)))(sorted(map(int, open('data.txt')))))))

# Part 2 - multiliner, but simple and clean
input = sorted(map(int, open('data.txt')))
counter = Counter({0: 1})
for i in input:
    counter[i] = counter[i - 3] + counter[i - 2] + counter[i - 1]
print(f'Part 2: {counter[max(input)]}')
