dice = list(map(int,input().split()))
n=int(input())
for i in range(n):
    qa,qb = map(int,input().split())
    if qa==dice[0]:
        if qb==dice[1]:
            print(dice[2])
        elif qb==dice[2]:
            print(dice[4])
        elif qb==dice[4]:
            print(dice[3])
        else:
            print(dice[1])
    elif qa==dice[1]:
        if qb==dice[0]:
            print(dice[3])
        elif qb==dice[3]:
            print(dice[5])
        elif qb==dice[5]:
            print(dice[2])
        else:
            print(dice[0])
    elif qa==dice[2]:
        if qb==dice[0]:
            print(dice[1])
        elif qb==dice[1]:
            print(dice[5])
        elif qb==dice[5]:
            print(dice[4])
        else:
            print(dice[0])
    elif qa==dice[3]:
        if qb==dice[0]:
            print(dice[4])
        elif qb==dice[4]:
            print(dice[5])
        elif qb==dice[5]:
            print(dice[1])
        else:
            print(dice[0])
    elif qa==dice[4]:
        if qb==dice[0]:
            print(dice[2])
        elif qb==dice[2]:
            print(dice[5])
        elif qb==dice[5]:
            print(dice[3])
        else:
            print(dice[0])
    else:
        if qb==dice[4]:
            print(dice[2])
        elif qb==dice[2]:
            print(dice[1])
        elif qb==dice[1]:
            print(dice[3])
        else:
            print(dice[4])
            
