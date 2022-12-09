#!/usr/bin/env python3

elves = [0]

with open("day1input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()

        if not line:
            elves.append(0)
        else:
            elves[-1] += int(line)

max1 = max(elves)
print(max1) # day 1 part 1
elves.pop(elves.index(max1))
max2 = max(elves)
elves.pop(elves.index(max2))
max3 = max(elves)
print(sum([max1, max2, max3])) # day 1 part 2