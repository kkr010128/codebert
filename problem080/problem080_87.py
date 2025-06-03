n=int(input())
zl,wl=[],[]
for i in range(n):
    x,y=map(int,input().split())
    z=x+y
    w=x-y
    zl.append(z)
    wl.append(w)
zl.sort()
wl.sort()
print(max(zl[-1]-zl[0],wl[-1]-wl[0]))