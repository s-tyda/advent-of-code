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
