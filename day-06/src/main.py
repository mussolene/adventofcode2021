import numpy as np

test = [3, 4, 3, 1, 2]
with open("day-06\data\input.txt", mode="r") as input:
    array = [list(map(int, row.strip().split(","))) for row in input][0]


def inc(array, days):

    offset = np.zeros(shape=9, dtype=np.int64)

    for t in array:
        offset[t] += 1

    fishes = sum(offset)

    for _ in range(days):
        increase = offset[0]
        fishes += increase

        for i in range(1, 9):
            offset[i - 1] = offset[i]

        offset[6] += increase
        offset[8] = increase

    return fishes


print(f"Part 1: {inc(array, 80)}")
print(f"Part 2: {inc(array, 256)}")
