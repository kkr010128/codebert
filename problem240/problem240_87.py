import sys
input()
d={}
nc=np=0
for ln in sys.stdin:
    p,S=ln.split()
    if p not in d:
        d[p]=[0,0]
    if not d[p][0]:
        if S=='AC':
            d[p][0]=1
            nc+=1
            np+=d[p][1]
        else:
            d[p][1]+=1

print(nc,np)
