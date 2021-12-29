from collections import Counter

with open("input/input6.txt", "r") as f:
    fish = []
    for line in f:
        for number in line.split(","):
            fish.append(int(number))

fc = Counter(fish)
fc = [fc[i] for i in range(9)]

def count_fish(fc, days):
    for i in range(days):
        fc = fc[1:] + [fc[0]]
        fc[6] += fc[8]
    return(sum(fc))

print(f"Part 1: How many lanternfish would there be after 80 days?: {count_fish(fc, days=80)}")

print(f"Part 1: How many lanternfish would there be after 256 days?: {count_fish(fc, days=256)}")
