from collections import Counter
from functools import reduce

with open("day-07\data\input.txt", mode="r") as input:
    array = list([list(map(int, row.strip().split(","))) for row in input])[0]

test = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

array.sort()

v = len(array) // 2
v = array[v]

fuel = 0
for i in array:
    fuel += abs(v - i)

print(f"Part 1: {fuel}")

sum1 = sum(array) // len(array)

minfuel = 0
for o in range(sum1 - 10, sum1 + 10):
    fuel = 0
    for i in array:
        fuel += sum(list([j for j in range(0, abs(sum1 - i) + 1)]))
    if fuel < minfuel:
        minfuel = fuel
    if minfuel == 0:
        minfuel = fuel


print(f"Part 2: {fuel}")
