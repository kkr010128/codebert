dice = list(input().split(' '))
a = list('NNNNWNNNWNNNENNNENNNWNNN')
for _ in range(int(input())):
    aa,bb  = input().split(' ')
    for i in a:
        if i == 'W':
            dice = [dice[2],dice[1],dice[5],dice[0],dice[4],dice[3]]
        elif i == 'S':
            dice = [dice[4],dice[0],dice[2],dice[3],dice[5],dice[1]]
        elif i == 'N':
            dice = [dice[1],dice[5],dice[2],dice[3],dice[0],dice[4]]
        elif i == 'E':
            dice = [dice[3],dice[1],dice[0],dice[5],dice[4],dice[2]]
        if dice[0] == aa and dice[1] == bb:
            print(dice[2])
            
