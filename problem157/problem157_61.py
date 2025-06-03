from collections import Counter
n=int(input())
a=list(map(int,input().split()))
b=dict(Counter([i-j for i,j in enumerate(a)]))
c=dict(Counter([i+j for i,j in enumerate(a)]))
cnt=0
for i in b:
  cnt+=b[i]*c.get(i,0)
print(cnt)