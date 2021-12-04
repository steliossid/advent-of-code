with open("input/input1.txt", "r") as f:
    data = [int(l.strip()) for l in f]


def find_increased(data):
    previous = data[0]
    increased = 0
    for current in data[1:]:
        if current > previous:
            increased += 1
        previous = current
    return increased


print(f"Part 1: The number of times a depth measurement increased {find_increased(data)} times")

sum_data = []
for i in range(len(data)):
    sum_data.append(sum(data[i:i+3]))

print(f"Part 2: The number of times a depth measurement increased {find_increased(sum_data)} times")
