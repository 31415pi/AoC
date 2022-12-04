# Advent of Code    2015 Day 2
# Code date:        3.12.2022
# https://adventofcode.com/2015/day/2
# Part 1: Wrapper
# Part 2: Ribbon
import re

wrapppr = 0
ribbn = 0
matcher = re.compile(r'^(\d+)x(\d+)x(\d+)$')
with open("D2_data.txt", 'r') as fd:
        for line in fd:
            match = matcher.search(line)
            x = sorted([int(part) for part in match.groups()])
#            Len, Wid, Hig = [int(part) for part in match.groups()]
#            x = sorted([Len, Wid, Hig])     
#            wrapppr += ( x[0]*x[1] + (Len*Wid + Wid*Hig + Hig*Len)*2 )
            wrapppr += (x[0]*x[1]*3 + (x[1]*x[2] + x[0]*x[2])*2) 
            ribbn += (2*(x[0] + x[1]) + x[0]*x[1]*x[2]) 
#            wrapppr += ( min([Len*Wid, Wid*Hig, Len*Hig]) + (Len*Wid + Wid*Hig + Hig*Len)*2 )
print('Wrapper = ', wrapppr, ' Ribbn = ', ribbn)


# Output: Wrapper =  1598415  Ribbn =  3812909
