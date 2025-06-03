dice = map(int, raw_input().split())
inst = raw_input()
 
def rolling(inst, dice):
    if inst == 'E':
        dice[5], dice[2], dice[0], dice[3] = dice[2], dice[0], dice[3], dice[5]
    elif inst == 'W':
        dice[5], dice[3], dice[0], dice[2] = dice[3], dice[0], dice[2], dice[5]
    elif inst == 'N':
        dice[5], dice[4], dice[0], dice[1] = dice[4], dice[0], dice[1], dice[5]
    elif inst == 'S':
        dice[5], dice[1], dice[0], dice[4] = dice[1], dice[0], dice[4], dice[5]
 
for i in range(len(inst)):
    rolling(inst[i], dice)
print dice[0]