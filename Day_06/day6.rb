# Day 6 Part 1
p IO.read("data.txt").split(?\n*2).sum{|x|x.chars.uniq.sort.join.strip.size}
# Day 6 Part 2
p IO.read("data.txt").split(?\n*2).sum{|g|g.split.map(&:chars).inject(:&).size}