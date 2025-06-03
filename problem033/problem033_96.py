def rotate(dice,d):
    if d == "N":
        temp = dice[0]
        dice[0] = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[4]
        dice[4] = temp
    elif d == "E":
        temp = dice[0]
        dice[0] = dice[3]
        dice[3] = dice[5]
        dice[5] = dice[2]
        dice[2] = temp
    elif d == "W":
        temp = dice[0]
        dice[0] = dice[2]
        dice[2] = dice[5]
        dice[5] = dice[3]
        dice[3] = temp
    elif d == "S":
        temp = dice[0]
        dice[0] = dice[4]
        dice[4] = dice[5]
        dice[5] = dice[1]
        dice[1] = temp
    return dice

dice = input().split()
dArr = list(input())
for i in range(len(dArr)):
    dice = rotate(dice,dArr[i])
print(dice[0])