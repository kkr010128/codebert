def rollDice(dice, direction):
    buf = [x for x in dice]
    if direction == "S":
        buf[0] = dice[4]
        buf[1] = dice[0]
        buf[4] = dice[5]
        buf[5] = dice[1]
    elif direction == "E":
        buf[0] = dice[3]
        buf[2] = dice[0]
        buf[3] = dice[5]
        buf[5] = dice[2]
    elif direction == "W":
        buf[0] = dice[2]
        buf[2] = dice[5]
        buf[3] = dice[0]
        buf[5] = dice[3]
    elif direction == "N":
        buf[0] = dice[1]
        buf[1] = dice[5]
        buf[4] = dice[0]
        buf[5] = dice[4]

    for i in range(6):
        dice[i] = buf[i]


def rollDiceSide(dice):
    buf = [x for x in dice]
    buf[1] = dice[2]
    buf[2] = dice[4]
    buf[3] = dice[1]
    buf[4] = dice[3]

    for i in range(6):
        dice[i] = buf[i]


d = list(map(int, input().split()))
n = int(input())

for i in range(n):
    q1, q2 = list(map(int, input().split()))

    wq = d.index(q1)
    if wq == 1:
        rollDice(d, "N")
    elif wq == 2:
        rollDice(d, "W")
    elif wq == 3:
        rollDice(d, "E")
    elif wq == 4:
        rollDice(d, "S")
    elif wq == 5:
        rollDice(d, "S")
        rollDice(d, "S")

    wq = d.index(q2)
    if wq == 2:
        rollDiceSide(d)
    elif wq == 3:
        rollDiceSide(d)
        rollDiceSide(d)
        rollDiceSide(d)
    elif wq == 4:
        rollDiceSide(d)
        rollDiceSide(d)

    print(d[2])


