with open("2022\day-03\data\input.txt", mode="r") as input:
    array = [row.strip() for row in input.read().split("\n")]

with open("2022\day-03\data\/testinput.txt", mode="r") as input:
    testarray = [row.strip() for row in input.read().split("\n")]


cost = 0
for i in array:
    length = len(i)
    left = int(length / 2)
    leftstring = i[:left]
    rightstring = i[left:]
    for j in range(0, len(leftstring)):
        if leftstring[j] in rightstring:
            cost += ord(i[j]) - 96 if ord(i[j]) >= 97 else ord(i[j]) - 38
            break
cost2 = 0
for i in range(0, len(array), 3):

    slicearray = array[i : i + 3]
    j = slicearray[0]
    for k in range(0, len(j)):
        if j[k] in array[i + 1] and j[k] in array[i + 2] and j[k] in array[i]:
            cost2 += ord(j[k]) - 96 if ord(j[k]) >= 97 else ord(j[k]) - 38
            break

print(f"Part 1 {cost}")
print(f"Part 2 {cost2}")
