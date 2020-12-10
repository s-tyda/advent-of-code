import strutils
import combinations

let file = readFile("data.txt").splitLines()

# Part 1
for x in combinations(file, 2):
    var a = parseInt(x[0])
    var b = parseInt(x[1])
    if a + b == 2020:
        echo "Part 1: ", a * b
        break

# Part 2
for x in combinations(file, 3):
    var a = parseInt(x[0])
    var b = parseInt(x[1])
    var c = parseInt(x[2])
    if a + b + c == 2020:
        echo "Part 2: ", a * b * c
        break
