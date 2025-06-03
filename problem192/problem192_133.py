import collections
a=int(input())
b=list(map(int,input().split()))

c=collections.Counter(b)

n,m=zip(*c.most_common())
n,m=list(n),list(m)
result=0
for i in range(len(m)):
    result+=(m[i]*(m[i]-1))//2

for i in b:
    print(result-c[i]+1)
