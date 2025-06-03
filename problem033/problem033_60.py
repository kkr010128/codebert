# ['表面', '南面', '東面', '西面', '北面', '裏面']
dice = input().split()
com = [c for c in input()]

rolling = {
    'E': [3, 1, 0, 5, 4, 2],
    'W': [2, 1, 5, 0, 4, 3],
    'S': [4, 0, 2, 3, 5, 1],
    'N': [1, 5, 2, 3, 0, 4]
}

for c in com:
    dice = [dice[i] for i in rolling[c]]

print(dice[0])
