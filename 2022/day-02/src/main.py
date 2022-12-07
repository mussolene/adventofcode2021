with open("2022\day-02\data\input.txt", mode="r") as input:
    array = [row.split() for row in input.read().split("\n")]

first = ["A", "B", "C"]
second = ["X", "Y", "Z"]
score = 0
score2 = 0
for i in array:
    step = i
    firststep = first.index(step[0])
    secondstep = second.index(step[1])

    score += secondstep + 1
    score += (secondstep - firststep + 1 + 3) % 3 * 3

    score2 += secondstep * 3
    score2 += (firststep + (secondstep - 1) + 3) % 3
    score2 += 1


print(f"Part 1 {score}")
print(f"Part 2 {score2}")
