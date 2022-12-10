with open("input/input2.txt", "r") as f:
    data = [l.strip() for l in f]

commands = []
values = []
for line in data:
    cmd_val = line.split()
    commands.append(cmd_val[0])
    values.append(int(cmd_val[1]))

horizontal_pos = 0
depth_pos = 0
for i in range(len(data)):
    if commands[i] == "forward":
        horizontal_pos += values[i]
    elif commands[i] == "down":
        depth_pos += values[i]
    else:
        depth_pos -= values[i]

print(f"Part 1: Multiply your final horizontal position by your final depth: {horizontal_pos*depth_pos}")

horizontal_pos = 0
depth_pos = 0
aim = 0
for i in range(len(data)):
    if commands[i] == "forward":
        horizontal_pos += values[i]
        depth_pos += aim * values[i]
    elif commands[i] == "down":
        aim += values[i]
    else:
        aim -= values[i]

print(f"Part 2: Multiply your final horizontal position by your final depth: {horizontal_pos*depth_pos}")
