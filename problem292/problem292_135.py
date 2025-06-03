from itertools import accumulate

N=int(input())
d=[int(i) for i in input().split()]
hp=[]

for i in range(N):
    for j in range(N):
        if i>j:
            hp.append(d[i]*d[j])
l=list(accumulate(hp))
print(l[-1])