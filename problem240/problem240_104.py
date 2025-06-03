n,m=map(int,input().split())
data=[0]*n
count,wa=0,0
for i in range(m):
    p,a=input().split()
    p=int(p)-1
    if type(data[p]) is int:
        if a=='WA':
            data[p]+=1
        else:
            wa+=data[p]
            data[p]=''
            count+=1
print(count,wa)