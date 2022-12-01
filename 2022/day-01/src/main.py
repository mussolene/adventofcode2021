with open("2022\day-01\data\input.txt", mode="r") as input:
    array = [sum([int(i) for i in row.split()]) for row in input.read().split("\n\n")]
    array.sort()
    maxelf = array[-1]
    max3elf = array[-1] + array[-2] + array[-3]

print(f"Part 1 :{maxelf}")
print(f"Part 2 :{max3elf}")
