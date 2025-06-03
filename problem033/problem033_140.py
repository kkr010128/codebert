u,s,e,w,n,b = list(map(int, input().split()))
rolls = input()

for roll in rolls:
    if roll == 'N':
        n,u,e,w,b,s = u,s,e,w,n,b
    elif roll == 'S':
        s,b,e,w,u,n = u,s,e,w,n,b
    elif roll == 'E':
        e,s,b,u,n,w = u,s,e,w,n,b
    elif roll == 'W':
        w,s,u,b,n,e = u,s,e,w,n,b
    else:
        print('Error')
        raise(-1)

print(u)