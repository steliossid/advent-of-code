import numpy as np

with open("input/input8.txt") as f:
    data = []
    for line in f:
        for digits in line.split("|")[1].split():
            data.append(digits)

numbers = ["cagedb", "ab", "gcdfa", "fbcad", "eafb", "cdfbe", "cdfgeb", "dab", "acedgfb", "cefabd"]

digits_size = [len(l) for l in numbers]

unique_numbers = []
for i, size in enumerate(digits_size):
    if size not in digits_size[:i]+digits_size[i+1:]:
        unique_numbers.append(i)

data_size = [len(l) for l in data]

count = sum([1 for size in data_size if size in [digits_size[i] for i in unique_numbers]])
print(f"Part 1: {count}")