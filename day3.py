with open("input/input3.txt", "r") as f:
    data = [list(l.strip()) for l in f]

n_bits = len(data[0])

gamma_rate = ""
epsilon_rate = ""
for i in range(n_bits):
    ones = 0
    zeros = 0
    for sequence in data:
        if sequence[i] == "1":
            ones += 1
        else:
            zeros += 1
    if ones > zeros:
        gamma_rate += "1"
        epsilon_rate += "0"
    else:
        gamma_rate += "0"
        epsilon_rate += "1"

print(f"Part 1: What is the power consumption of the submarine?: {int(gamma_rate, 2) * int(epsilon_rate, 2)}")


def life_support_rating(data, oxygen):
    for i in range(n_bits):
        if len(data) == 1:
            return int("".join(data[0]), 2)
        ones = 0
        zeros = 0
        for sequence in data:
            if sequence[i] == "1":
                ones += 1
            else:
                zeros += 1
        if ones > zeros:
            if oxygen:
                data = list(filter(lambda x: x[i] == "1", data))
            else:
                data = list(filter(lambda x: x[i] == "0", data))
        elif ones < zeros:
            if oxygen:
                data = list(filter(lambda x: x[i] == "0", data))
            else:
                data = list(filter(lambda x: x[i] == "1", data))
        else:
            if oxygen:
                data = list(filter(lambda x: x[i] == "1", data))
            else:
                data = list(filter(lambda x: x[i] == "0", data))


oxygen_rating = life_support_rating(data, oxygen=True)
co2_rating = life_support_rating(data, oxygen=False)
print(f"Part 2: What is the life support rating of the submarine?: {oxygen_rating*co2_rating}")
