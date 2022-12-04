# Advent of Code    2015 Day 2
# Code date:        3.12.2022
# https://adventofcode.com/2015/day/2
# Part 1:
import re

wrapppr = 0
matcher = re.compile(r'^(\d+)x(\d+)x(\d+)$')
with open("D2_data.txt", 'r') as fd:
        for line in fd:
            match = matcher.search(line)
            Len, Wid, Hig = [int(part) for part in match.groups()]
            wrapppr += ( min([Len*Wid, Wid*Hig, Len*Hig]) + (Len + Wid + Hig)*2 )
#            x = sorted([Len, Wid, Hig])
#            wrapppr += ( x[0]*x[1] + (Len*Wid + Wid*Hig + Hig*Len)*2 )
            
print(wrapppr)
