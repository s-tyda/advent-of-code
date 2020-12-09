import re
# Part 1
print("Part 1: {}".format(sum([1 if all([i in x for i in ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']]) else 0 for x in open('data.txt').read().split("\n\n")])))

# Part 2
print("Part 2: {}".format(sum(
    [1 if all([i in x for i in ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']]) and
                (lambda line: 1 if
                ((1920 <= int(line['byr']) <= 2002) and
                 (2010 <= int(line['iyr']) <= 2020) and
                 (2020 <= int(line['eyr']) <= 2030) and
                 (((line['hgt'][-2:] == 'cm') and (150 <= int(line['hgt'][:-2]) <= 193)) or
                  ((line['hgt'][-2:] == 'in') and (59 <= int(line['hgt'][:-2]) <= 76))) and
                 (line['hcl'][0] == '#' and all([x.isalnum() for x in line['hcl'][1:]])) and
                 (line['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']) and
                 (len(line['pid']) == 9 and all([x.isdigit() for x in line['pid']])))
                else 0)
                ({j.split(':')[0]: j.split(':')[1] for j in re.split('\n| ', x) if ':' in j})
       else 0 for x in open('data.txt').read().split("\n\n")]
)))

# Part 2 - regex
print("Part 2: {}".format(sum(all(re.search(i, x) for i in [
    r"byr:(19[2-9]\d|200[0-2])",
    r"iyr:20(1\d|20)",
    r"eyr:20(2\d|30)",
    r"hgt:(1([5-8]\d|9[0-3])cm|(59|6\d|7[0-6])in)",
    r"hcl:#[0-9a-f]{6}",
    r"ecl:(amb|blu|brn|gry|grn|hzl|oth)",
    r"pid:\d{9}\b"
])for x in open("data.txt").read().split("\n\n"))))
