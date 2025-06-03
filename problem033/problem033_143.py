def get_dice(pips):
    return [[0, pips[4], 0, 0], 
                   [pips[3], pips[0], pips[2], pips[5]], 
                   [0, pips[1], 0, 0]]

def move_e(dice):
    dice[1] = dice[1][3:] + dice[1][:3]
    return dice

def move_n(dice):
    return [[0,          dice[1][1], 0, 0],
            [dice[1][0], dice[2][1], dice[1][2], dice[0][1]],
            [0,                 dice[1][3], 0, 0]]

def move_s(dice):
    return [[0,          dice[1][3], 0, 0],
            [dice[1][0], dice[0][1], dice[1][2], dice[2][1]],
            [0,                 dice[1][1], 0, 0]]

def move_w(dice):
    dice[1] = dice[1][1:] + dice[1][:1]
    return dice

func = {'E':move_e,'N':move_n,'S':move_s,'W':move_w}

dice = get_dice(list(map(int, input().split())))

for c in input():
    dice = func[c](dice)

print(dice[1][1])