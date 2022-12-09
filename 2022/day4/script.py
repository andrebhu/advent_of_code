#!/usr/bin/env python3

def func(a, b, c, d):
    if a <= c and d <= b:
        return True
    elif c <= a and b <= d:
        return True
    return False

pairs = 0
with open("input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()

        s1, s2 = line.split(",")
        a, b = s1.split("-")
        c, d = s2.split("-")
        if func(int(a), int(b), int(c), int(d)):
            pairs += 1
print(pairs)

def overlap(a, b, c, d):
    m = [0] * 100
    for i in range(a, b + 1):
        m[i] = 1
    for j in range(c, d + 1):
        if m[j] == 1:
            return True
    return False

total = 0
with open("input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        s1, s2 = line.split(",")
        a, b = s1.split("-")
        c, d = s2.split("-")

        if overlap(int(a), int(b), int(c), int(d)):
            total += 1
print(total)