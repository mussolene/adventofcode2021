from collections import Counter

bingoNum = []
arrayOfCard = []
card = []
won_card = []
won_num = []

with open("day-04\data\input.txt", mode="r") as input:
    for row in input:
        row.replace("  ", " ")
        if not bingoNum:
            bingoNum = list(map(int, row.strip().split(sep=",")))
            continue

        if row.strip():
            card.append(list(map(int, row.strip().split(sep=" "))))
        else:
            if card:
                arrayOfCard.append([x for x in card])
                card = []


for i in bingoNum:
    for j in range(len(arrayOfCard)):
        card = arrayOfCard[j]
        if card in won_card:
            continue
        for row in card:
            for col in row:
                if i == col:
                    row[row.index(col)] = "X"
        if max(
            len(Counter(a).keys()) == 1 or len(Counter(b).keys()) == 1
            for a, b in zip(card, zip(*card))
        ):
            won_card.append(card)
            won_num.append(i)

print(
    f'Part 1: {won_num[0] * sum([d for x in won_card[0] for d in x if not d == "X"])}'
)
print(
    f'Part 2: {won_num[-1] * sum([d for x in won_card[-1] for d in x if not d == "X"])}'
)
