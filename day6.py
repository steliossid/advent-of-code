from _collections import Counter

with open("input/input6.txt", "r") as f:
    fish = []
    for line in f:
        for number in line.split(","):
            fish.append(int(number))

fish = Counter(fish)


def count_fish(fish, days):
    for day in range(days):
        n_current = len(fish)
        for i in range(n_current):
            if fish[i] == 0:
                fish[i] = 6
                fish.append(8)
            else:
                fish[i] -= 1
    return len(fish)


print(f"Part 1: How many lanternfish would there be after 80 days?: {count_fish(fish, days=80)}")

print(f"Part 1: How many lanternfish would there be after 256 days?: {count_fish(fish, days=256)}")
