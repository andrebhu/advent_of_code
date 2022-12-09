#!/usr/bin/env python3

class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.files = []
        self.directories = []

    def get_files_size(self):
        size = 0
        for f in self.files:
            size += f.size
        return size

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)


root = Directory("/")
current_directory = root

with open("input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        data = line.split(" ")

        # cd or ls commands
        if data[0] == "$":
            if data[1] == "cd":
                if data[2] == "..": # jump up directory
                    current_directory = current_directory.parent                    
                elif data[2] == "/": # go to root
                    current_directory = root
                else: # enter directory
                    d = None
                    for d in current_directory.directories:
                        if d.name == data[2]:
                            current_directory = d
            elif data[1] == "ls": # list files and directories
                pass
        else:
            if data[0] == "dir": # directories
                current_directory.directories.append(Directory(data[1], current_directory))
            else: # files
                current_directory.files.append(File(data[1], data[0]))

# get sizes
TOTAL = 0

d_s = {}


def get_total_size(d):
    global TOTAL

    files_size = d.get_files_size()
    
    if len(d.directories) == 0:
        d_s[d.name] = files_size
        if files_size < 100000:
            TOTAL += files_size
        return d.get_files_size()
    else:
        d_total = 0
        d_total += files_size

        for i in d.directories:
            d_total += get_total_size(i)

        if d_total < 100000:
            TOTAL += d_total
        d_s[d.name] = d_total
        return d_total

total_size = get_total_size(root)
print(TOTAL)


minimum = 30000000 - (70000000 - total_size)


possible = []
for k, v in d_s.items():
    if v > minimum:
        possible.append(v)
    
print(min(possible))

# 31148261 too high
# 3696336