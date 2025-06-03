import sys
 
x,y = map(int,input().split())
 
for n in range(x+1):
    kame = x - n
 
    tsuru_leg = n*2
    kame_leg = kame*4
 
    if y == tsuru_leg + kame_leg:
        print('Yes')
        sys.exit()
 
print('No')