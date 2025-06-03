import collections
N=int(input())
A=list(map(int,input().split()))
c=collections.Counter(A)

#全体の数列について答えを求めるnC2=n(n-1)/2
ALL=0
for i in c.values():
  if i>1:
    ALL += i*(i-1)//2

#各要素が影響する分を求める
for i in A:
  if c[i]>2:
    print(ALL-c[i]+1)
  elif c[i]==2:
    print(ALL-1)
  else:
    print(ALL)