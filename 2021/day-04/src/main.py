from collections import Counter

bingoNum = []
arrayOfCard = []
card = []
won_card = []
won_num = []

with open("day-04\data\input.txt", mode="r") as input:
    array = list([row.strip() for row in input])
    bingoNum = list(map(int, array[0].split(sep=",")))
    for row in array[2:]:
        if row.replace("  ", " "):
            card.append(list(map(int, row.strip().split(sep=" "))))
        else:
            arrayOfCard.append([x for x in card])
            card = []


for i in bingoNum:
    for j in range(len(arrayOfCard)):
        if arrayOfCard[j] in won_card:
            continue

        arrayOfCard[j] = [
            ["X" if row[z] == i else row[z] for z in range(len(row))]
            for row in arrayOfCard[j]
        ]

        if max(
            len(Counter(a).keys()) == 1 or len(Counter(b).keys()) == 1
            for a, b in zip(arrayOfCard[j], zip(*arrayOfCard[j]))
        ):
            won_card.append(arrayOfCard[j])
            won_num.append(i)

print(
    f'Part 1: {won_num[0] * sum([d for x in won_card[0] for d in x if not d == "X"])}'
)
print(
    f'Part 2: {won_num[-1] * sum([d for x in won_card[-1] for d in x if not d == "X"])}'
)
