#!/usr/bin/env python3

'''
                [M]     [V]     [L]
[G]             [V] [C] [G]     [D]
[J]             [Q] [W] [Z] [C] [J]
[W]         [W] [G] [V] [D] [G] [C]
[R]     [G] [N] [B] [D] [C] [M] [W]
[F] [M] [H] [C] [S] [T] [N] [N] [N]
[T] [W] [N] [R] [F] [R] [B] [J] [P]
[Z] [G] [J] [J] [W] [S] [H] [S] [G]
 1   2   3   4   5   6   7   8   9 
'''

stack_1 = ["Z", "T", "F", "R", "W", "J", "G"]
stack_2 = ["G", "W", "M"]
stack_3 = ["J", "N", "H", "G"]
stack_4 = ["J", "R", "C", "N", "W"]
stack_5 = ["W", "F", "S", "B", "G", "Q", "V", "M"]
stack_6 = ["S", "R", "T", "D", "V", "W", "C"]
stack_7 = ["H", "B", "N", "C", "D", "Z", "G", "V"]
stack_8 = ["S", "J", "N", "M", "G", "C"]
stack_9 = ["G", "P", "N", "W", "C", "J", "D", "L"]

stacks = [
    stack_1,
    stack_2,
    stack_3,
    stack_4,
    stack_5,
    stack_6,
    stack_7,
    stack_8,
    stack_9
]


def move2(num, s1, s2):
    stacks[s2 - 1].extend(stacks[s1 - 1][-1 * num:])
    stacks[s1 - 1] = stacks[s1 - 1][:-1 * num]




# def move(num, s1, s2):
#     for _ in range(num):
#         stacks[s2 - 1].append(stacks[s1 - 1].pop(-1))

with open("modified.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()

        data = line.split(" ")
        num = int(data[1])
        s1 = int(data[3])
        s2 = int(data[5])
        move2(num, s1, s2)

for s in stacks:
    print(s[-1], end="")