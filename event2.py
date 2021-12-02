with open("input2.txt", mode="r") as input:
    array = list([row.strip().split() for row in input])
# task1
horizontal = 0
depth = 0

for i in array:
    if i[0] == "forward":
        horizontal = horizontal + int(i[1])
    if i[0] == "up":
        depth = depth - int(i[1])
    if i[0] == "down":
        depth = depth + int(i[1])
print(horizontal)
print(depth)
print(depth * horizontal)

# task2
horizontal = 0
depth = 0
aim = 0

for i in array:
    if i[0] == "forward":
        horizontal = horizontal + int(i[1])
        depth = depth + (int(i[1]) * aim)
    if i[0] == "up":
        aim = aim - int(i[1])
    if i[0] == "down":
        aim = aim + int(i[1])

print(horizontal)
print(depth)
print(aim)
print(depth * horizontal)
