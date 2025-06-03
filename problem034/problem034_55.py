dice = input().split()
dice.insert(4, dice.pop(3))
right = []


def rightSearch(up, front):
    index_up = dice.index(up)
    index_front = dice.index(front)
    if 1 <= index_up <= 4 and 1 <= index_front <= 4:
        if index_up == 4 and index_front == 1:
            return dice[0]
        if index_up == 1 and index_front == 4:
            return dice[5]
        if index_up < index_front:
            return dice[0]
        else:
            return dice[5]
    elif (index_front == 0 or index_front == 5) and (index_up != 0 or index_up != 5):
        if index_front == 0:
            if index_up == 1:
                return dice[4]
            else:
                return dice[index_up - 1]
        else:
            if index_up == 4:
                return dice[1]
            else:
                return dice[index_up + 1]
    else:
        if index_up == 0:
            if index_front == 4:
                return dice[1]
            else:
                return dice[index_front + 1]
        else:
            if index_front == 1:
                return dice[4]
            else:
                return dice[index_front - 1]


number = int(input())
for i in range(number):
    up, front = input().split()
    right.append(rightSearch(up, front))

for r in right:
    print(r)
