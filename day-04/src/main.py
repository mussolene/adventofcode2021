from collections import Counter

bingoNum = []
arrayOfCard = []
card = []
with open("day-04\data\input.txt", mode="r") as input:
    for row in input:
        if not bingoNum:
            bingoNum = list(map(int, row.strip().split(sep=",")))
            continue

        if row.strip():
            card.append(list(map(int, row.strip().split(sep=" "))))
        else:
            if card:
                arrayOfCard.append([x for x in card])
                card = []


def checkcard(card):
    for row in card:
        if len(Counter(row).keys()) == 1:
            return True
    matrix = list(zip(*card))
    for row in matrix:
        if len(Counter(row).keys()) == 1:
            return True
    return False


def sumcard(card):
    s = 0
    for row in card:
        for column in row:
            if not column == "X":
                s = s + column
    return s


won_card = []
won_num = []
for i in bingoNum:
    for j in range(0, len(arrayOfCard)):
        card = arrayOfCard[j]
        if card in won_card:
            continue
        for row in card:
            for col in row:
                if i == col:
                    row[row.index(col)] = "X"
        if checkcard(card):
            won_card.append(card)
            won_num.append(i)

print(f"Part 1: {won_num[0] * sumcard(won_card[0])}")
print(f"Part 2: {won_num[-1] * sumcard(won_card[-1])}")
