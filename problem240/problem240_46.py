n,m=map(int,input().split())

data=[0]*n
s=set()
sum_wa=0

for i in range(m):
    p,a=input().split()
    p=int(p)-1
    if p in s:
        continue
    else:
        if a=='WA':
            data[p]+=1
        else:
            sum_wa+=data[p]
            s.add(p)

print(len(s),sum_wa)