x,y = map(int,input().split())

ans = 0

for n in range(x+1):
    kame = x - n

    tsuru_leg = n*2
    kame_leg = kame*4

    if y == (tsuru_leg+kame_leg):
        ans = ans + 1

if ans == 0:
    print('No')
else:
    print('Yes') 