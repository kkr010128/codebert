import collections

N=int(input())
A=list(map(int,input().split()))
B=collections.Counter(A)
C=sum([x*(x-1)//2 for x in B.values()])

for i in A:
  temp=B[i]
  print(C-(temp*(temp-1)//2-(temp-1)*(temp-2)//2))