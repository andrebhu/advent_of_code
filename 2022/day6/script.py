#!/usr/bin/env python3

chars_processed = 0

last_4 = []

with open("input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        for c in line:

            if len(set(last_4)) == 4:
                print(chars_processed)
                break

            if len(last_4) < 4:
                last_4.append(c)
            else:
                last_4.append(c)
                last_4.pop(0)
            chars_processed += 1

last_14 = []
chars_processed = 0

with open("input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        for c in line:

            if len(set(last_14)) == 14:
                print(chars_processed)
                break

            if len(last_14) < 14:
                last_14.append(c)
            else:
                last_14.append(c)
                last_14.pop(0)
            chars_processed += 1

