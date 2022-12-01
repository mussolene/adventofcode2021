with open("day-09\data\/test.txt", mode="r") as input:
    array = [[int(s) for s in row.strip()] for row in input]

row, col = len(array), len(array[0])

m = []
idexAr = []


def getbound(array, x, y, min=9):
    row, col = len(array), len(array[0])

    if x >= row or x < 0:
        return min
    if y >= col or y < 0:
        return min

    if x >= row or x < 0:
        return min
    if y >= col or y < 0:
        return min

    return array[x][y]


def getpoint(array, x, y):
    basin = []

    a = x
    b = y
    while getbound(array, a, b) < 9:
        if not (a, b) in basin:
            basin.append((a, b))
        while getbound(array, a, b) < 9:
            if not (a, b) in basin:
                basin.append((a, b))
            b += 1
        b = y
        while getbound(array, a, b) < 9:
            if not (a, b) in basin:
                basin.append((a, b))
            b -= 1
        a += 1

    a = x
    b = y
    while getbound(array, a, b) < 9:
        if not (a, b) in basin:
            basin.append((a, b))
        while getbound(array, a, b) < 9:
            if not (a, b) in basin:
                basin.append((a, b))
            b += 1
        b = y
        while getbound(array, a, b) < 9:
            if not (a, b) in basin:
                basin.append((a, b))
            b -= 1
        a -= 1

    return basin


def getpointrec(ar, i, j, lengthx, lengthy):
    m = []

    if i > lengthx or j > lengthy:
        return m

    m.append((i, j))
    if (
        getbound(ar, i, j + 1, 8) < 9
        and getbound(ar, i, j - 1, 8) < 9
        and getbound(ar, i + 1, j, 8) < 9
        and getbound(ar, i - 1, j, 8) < 9
    ):
        r = getpointrec(ar, i + 1, j, lengthx, lengthy)
        l = getpointrec(ar, i, j + 1, lengthx, lengthy)
        u = getpointrec(ar, i - 1, j, lengthx, lengthy)
        d = getpointrec(ar, i, j - 1, lengthx, lengthy)
        for z in r:
            m.append(z)
        for z in u:
            m.append(z)
        for z in l:
            m.append(z)
        for z in d:
            m.append(z)
    return m


for i in range(row):
    for j in range(col):
        if (
            array[i][j] < getbound(array, i, j + 1)
            and array[i][j] < getbound(array, i, j - 1)
            and array[i][j] < getbound(array, i + 1, j)
            and array[i][j] < getbound(array, i - 1, j)
        ):
            m.append(array[i][j])
            idexAr.append((i, j))


basinar = []
lengthx = row
lengthy = col
for i in idexAr:
    a, b = i
    m = getpointrec(array, a, b, lengthx, lengthy)
    basinar.append(m)

print(len(basinar))
print(f"Part 1: {sum(m) + len(m)}")
