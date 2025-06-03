mask = {'N':(1, 5, 2, 3, 0, 4), 'E':(3, 1, 0, 5, 4, 2), 'S':(4, 0, 2, 3, 5, 1), 'W':(2, 1, 5, 0, 4,3)}

dice = input().split()

for c in input():
    dice = [dice[i] for i in mask[c]]

print(dice[0])