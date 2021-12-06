from collections import Counter

with open("input/input5.txt", "r") as f:
    x1_data = []
    y1_data = []
    x2_data = []
    y2_data = []
    for line in f:
        line_split = line.split()
        line_x1y1 = line_split[0].split(",")
        line_x1 = int(line_x1y1[0])
        line_y1 = int(line_x1y1[1])
        line_x2y2 = line_split[2].split(",")
        line_x2 = int(line_x2y2[0])
        line_y2 = int(line_x2y2[1])
        x1_data.append(line_x1)
        y1_data.append(line_y1)
        x2_data.append(line_x2)
        y2_data.append(line_y2)

x1_new = []
y1_new = []
x2_new = []
y2_new = []
n = len(x1_data)
for i in range(n):
    if x1_data[i] == x2_data[i] or y1_data[i] == y2_data[i]:
        x1_new.append(x1_data[i])
        y1_new.append(y1_data[i])
        x2_new.append(x2_data[i])
        y2_new.append(y2_data[i])

n = max(x1_new + y1_new + x2_new + y2_new)
lines = [[0 for i in range(n+1)] for j in range(n+1)]

lines_points = []
for x1, y1, x2, y2 in zip(x1_new, y1_new, x2_new, y2_new):
    if x1 == x2:
        if y1 < y2:
            for y in range(y1, y2+1):
                lines_points.append([x1, y])
        else:
            for y in range(y2, y1+1):
                lines_points.append([x1, y])
    if y1 == y2:
        if x1 < x2:
            for x in range(x1, x2+1):
                lines_points.append([x, y1])
        else:
            for x in range(x2, x1+1):
                lines_points.append([x, y1])

n_points_overlap = sum([1 for item, count in Counter(tuple(item) for item in lines_points).items() if count >= 2])
print(f"Part 1: Consider only horizontal and vertical lines. "
      f"At how many points do at least two lines overlap?: {n_points_overlap}")
