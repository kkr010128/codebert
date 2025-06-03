dice = list(map(int, input().split()))
command = str(input())

for c in command:
    if (c == 'S'): ##2651 --> 1265
        dice[1],dice[5],dice[4],dice[0] = dice[0],dice[1],dice[5],dice[4]
    elif(c == 'N'):
        dice[0],dice[1],dice[5],dice[4] = dice[1],dice[5],dice[4],dice[0]
    elif (c == 'W'): ##4631 -- > 1463
        dice[3], dice[5], dice[2],dice[0] = dice[0], dice[3], dice[5], dice[2]
    else:
        dice[0], dice[3], dice[5], dice[2] = dice[3], dice[5], dice[2],dice[0] 
print(dice[0])
