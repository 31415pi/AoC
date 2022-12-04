//Advent of Code    2015 Day 1
//Code date:        3.12.2022
//https://adventofcode.com/2015/day/1
//Part 1.
//Part 2: Uncomment 6,9,14-17.
//line 5 is for the iter.
from functools import partial
total = 0
//sum = 0
with open("D1_data.txt", 'r') as f:
    for floor in iter(partial(f.read, 1), ''):
//        sum +=1
        if (floor == "("):
            total +=1
        else:
            total -=1
//            if (total == -1):
//                print("First went to the basermenter:")
//                print(sum)
//                exit()
print("total:")
print(total)
