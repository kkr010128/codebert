from collections import defaultdict
d=defaultdict(list)
n ,m =list(map(int,input().split()))
h=list(map(int,input().split()))
for i in range(m):
    a,b=list(map(int,input().split()))
    d[a].append(b)
    d[b].append(a)
s=0
for c in d:
    k=0
    for v in d[c]:
        if h[c-1]<=h[v-1]:
            k=1
            break
    #print(c,k,d)
    if k==0:
        s+=1
s+=n-len(d)
print(s)