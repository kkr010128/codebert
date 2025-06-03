n = int(input())
lx = list(map(int,input().split()))

lc=[]
for i in range(1,101):
    c = 0
    for x in lx:
        c += (i-x)**2
    lc.append(c)

print(min(lc))
