with open("day-08\data\/input.txt", mode="r") as input:
    array = [row.strip() for row in input]
    array = [row.split(" | ") for row in array]
    data = [row[0].split(" ") for row in array]
    output = [row[1].split(" ") for row in array]


def get(data, count):
    ret = []
    for i in data:
        if len(i) == count:
            a = [ord(b) for b in i]
            a.sort()
            ret.append(a)
    return ret


part1 = 0
part2 = 0
for m in range(0, len(data)):
    i = data[m]
    o = output[m]
    d1 = set(get(i, 2)[0])
    d7 = set(get(i, 3)[0])
    d8 = set(get(i, 7)[0])
    d4 = set(get(i, 4)[0])

    a = d7 - d1

    candidate235 = get(i, 5)
    candidate069 = get(i, 6)

    for j in candidate235:
        can = set(j)
        if len(can - d1) == 3:
            d3 = can
        elif len(can - d7 - d4) == 2:
            d2 = can
        elif len(can - d7 - d4) == 1:
            d5 = can

    for j in candidate069:
        can = set(j)
        if len(can - d3) == 1:
            d9 = can
        elif len(can - d7) == 3:
            d0 = can
        elif len(d8 - can - d7) == 0:
            d6 = can

    a = [[ord(g) for g in h] for h in o]
    pp = ""
    for b in a:
        b.sort()
        p = set(b)
        if p == d1 or p == d7 or p == d8 or p == d4:
            part1 += 1

        if p == d1:
            pp = pp + "1"

        elif p == d2:
            pp = pp + "2"

        elif p == d3:
            pp = pp + "3"

        elif p == d4:
            pp = pp + "4"

        elif p == d5:
            pp = pp + "5"
        elif p == d6:
            pp = pp + "6"

        elif p == d7:
            pp = pp + "7"

        elif p == d8:
            pp = pp + "8"

        elif p == d9:
            pp = pp + "9"

        elif p == d0:
            pp = pp + "0"

    part2 += int(pp)

print(part1)
print(part2)
