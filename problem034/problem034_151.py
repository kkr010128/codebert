dice_init = input().split()
dicry = {'search':"152304",'hittop':'024135', 'hitfront':'310542'}
num = int(input())

def dicing(x):
    global dice
    dice = [dice[int(c)] for c in dicry[x]]

for _ in range(num):
    dice = dice_init
    top, front = map(int, input().split())
    while True:
        if int(dice[0]) == top and int(dice[1]) == front:
            break
        elif int(dice[0]) == top:
            dicing('hittop')
        elif int(dice[1]) == front:
            dicing('hitfront')
        else:
            dicing('search')
    print(dice[2])
