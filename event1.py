from os import abort

with open("input.txt", mode="r") as input:
    array = [row.strip() for row in input]

# 1 task
def sum_icrease(array):
    increase = 0
    for x in range(0, len(array)):
        if x == 0:
            continue
        a = array[x]
        b = array[x - 1]
        if int(a) > int(b):
            increase += 1
    return increase


increase = sum_icrease(array)
print(increase)

# 2 task
array_sum = []
length = len(array)
for x in range(0, length):
    if length - x <= 2:
        continue
    a = array[x]
    b = array[x + 1]
    c = array[x + 2]
    array_sum.append(int(a) + int(b) + int(c))


increase = sum_icrease(array_sum)
print(increase)
