import collections

n = int(input())
A = list(map(int,input().split()))
a = collections.Counter(A)
sum_ = sum(A)

Q = int(input())
B,C = [],[]
for i in range(Q):
  lis = list(map(int,input().split()))
  B.append(lis[0])
  C.append(lis[1])

for j,b in enumerate(B):
  sum_+=a[b]*(C[j]-b)
  a[C[j]]+=a[b]
  a[b]=0
  print(sum_)
  

