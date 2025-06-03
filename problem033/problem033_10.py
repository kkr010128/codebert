dice = [int(i) for i in input().split()]
directions = str(input())
for direction in directions:
    if direction == "N":
        dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]
    elif direction == "S":
        dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]           
    elif direction == "E":
        dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    else:
        dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
print(dice[0])
