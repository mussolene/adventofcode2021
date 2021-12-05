import collections
from collections import Counter

with open("day-05\data\input.txt", mode="r") as input:
    lines = list(
        [
            list(map(lambda x: list(map(int, x.split(","))), i))
            for i in [row.strip().split(" -> ") for row in input]
        ]
    )

diagram = collections.defaultdict(int)


def hl(diagram, y, x1, x2):
    res = 0
    for i in range(min(x1, x2), max(x1, x2) + 1):
        diagram[(i, y)] += 1
        if diagram[(i, y)] == 2:
            res += 1
    return res


def vl(diagram, y, x1, x2):
    res = 0
    for i in range(min(x1, x2), max(x1, x2) + 1):
        diagram[(y, i)] += 1
        if diagram[(y, i)] == 2:
            res += 1
    return res


def dl(diagram, x1, y1, x2, y2):
    res = 0
    for _ in range(abs(x2 - x1) + 1):
        diagram[(x1, y1)] += 1
        if diagram[(x1, y1)] == 2:
            res += 1

        x1 += 1 if x2 > x1 else -1
        y1 += 1 if y2 > y1 else -1
    return res


hv = 0
dia = 0

for line in lines:
    p1, p2 = line
    x1, y1 = p1
    x2, y2 = p2

    if x1 == x2:
        hv += vl(diagram, x1, y1, y2)
    elif y1 == y2:
        hv += hl(diagram, y1, x1, x2)

for line in lines:
    p1, p2 = line
    x1, y1 = p1
    x2, y2 = p2

    if x1 == x2 or y1 == y2:
        continue
    
    dia += dl(diagram, x1, y1, x2, y2)

print(f"Part 1: {hv}")
print(f"Part 2: {hv + dia}")
