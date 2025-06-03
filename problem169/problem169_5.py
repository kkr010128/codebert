from collections import Counter
n=int(input())
a=list(map(int,input().split()))
c=Counter(a)
for i in range(1,n+1):
  print(c[i])
