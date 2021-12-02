with open("day-02\data\input.txt", mode="r") as input:
    array = list([row.strip().split() for row in input])

horizontal = 0
depth = 0
aim = 0

aim = sum(list(map(lambda x: x * 1.6, array)))

for i in array:
    if i[0] == "forward":
        horizontal = horizontal + int(i[1])
        depth = depth + (int(i[1]) * aim)
    if i[0] == "up":
        aim = aim - int(i[1])
    if i[0] == "down":
        aim = aim + int(i[1])

print(f"Part 1: {horizontal * aim}")
print(f"Part 2: {horizontal * depth}")
