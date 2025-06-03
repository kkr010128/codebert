from collections import Counter
n=int(input())
a=list(map(int,input().split()))
jc=[0]*n
for i in range(n):
    jc[i]+=i+1-a[i]
jcc=Counter(jc)
count=0
for j in range(n):
    count+=jcc[a[j]+j+1]
print(count)
