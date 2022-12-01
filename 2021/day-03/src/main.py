with open("day-03\data\input.txt", mode="r") as input:
    array = list([list(map(int, row.strip())) for row in input])

# task 1
matrix_t = list(zip(*array))

gammab = []
epsilonb = []

for i in matrix_t:
    gammab.append(str(int(sum(list(i)) > len(i) / 2)))
    epsilonb.append(str(int(sum(list(i)) < len(i) / 2)))

gamma = int("".join(gammab), base=2)
epsilon = int("".join(epsilonb), base=2)

print(f"Part 1: {gamma * epsilon}")

# task 2
size = len(matrix_t)
ar = array
ar2 = array

for i in range(0, size):
    matrix_x = list(zip(*ar))
    size = len(matrix_x)
    s = sum(list(matrix_x[i]))
    l = len(matrix_x[i]) / 2

    if s == l:
        e = 1
    else:
        e = int(s > l)

    if len(ar) == 1:
        break

    ar = [x for x in ar if x[i] == e]


for i in range(0, size):
    matrix_c = list(zip(*ar2))
    size = len(matrix_c)
    s = sum(list(matrix_c[i]))
    l = len(matrix_c[i]) / 2

    if s == l:
        e = 0
    else:
        e = int(s < l)

    if len(ar2) == 1:
        break

    ar2 = [x for x in ar2 if x[i] == e]

o2 = int("".join([str(x) for x in ar[0]]), base=2)
scrubber = int("".join([str(x) for x in ar2[0]]), base=2)

print(f"Part 2: {o2 * scrubber}")
