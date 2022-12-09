#!/usr/bin/env python3

def find_similar(r1, r2):
    for c in r1:
        if c in r2:
            return c
    return None

scores = {}

for i, j in zip(range(1, 27), "abcdefghijklmnopqrstuvwxyz"):
    scores[j] = i

for i, j in zip(range(27, 53), "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    scores[j] = i

total = 0

with open("input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        
        k1, k2 = line[:len(line)//2], line[len(line)//2:]
        s = find_similar(k1, k2)
        total += scores[s]

print(total)


def find_badge(r1, r2, r3):
    r1_r2_sim = []
    for c in r1:
        if c in r2:
            r1_r2_sim.append(c)
    
    for c in r1_r2_sim:
        if c in r3:
            return c
    return None


total = 0
with open("input.txt", "r") as file:
    lines = file.readlines()
    for i in range(0, len(lines), 3):
        b = find_badge(lines[i], lines[i + 1], lines[i + 2])
        total += scores[b]

print(total)

