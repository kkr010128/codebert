nb=4
nf=3
nr=10
d = {}
n = int(input())
for i in range(n):
    [b,f,r,v] = map(int, input().split())
    key = "%2d %2d %2d"  % (b,f,r)
    if key in d:
        d[key] += v
    else:
        d[key] = v

for b in range(1,nb+1):
    for f in range(1,nf+1):
        for r in range(1,nr+1):
            key = "%2d %2d %2d" % (b,f,r)
            if key in d:
                print(" "+str(d[key]),end="")
            else:
                print(" "+str(0),end="")
            if r==nr:
                print()
            if r==nr and f==nf and b != nb:
                print('####################')