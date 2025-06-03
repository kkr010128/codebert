n,m=map(int,input().split())

data=[0]*n
s=set()

for i in range(m):
    p,a=input().split()
    p=int(p)-1
    if p in s:
        continue
    else:
        if a=='WA':
            data[p]-=1
        else:
            data[p]*=-1
            s.add(p)

print(len(s),sum([data[i] for i in range(n) if data[i]>0]))