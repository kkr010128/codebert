N, K = list(map(int, input().split(' ')))

A=[0]*N
D=[0]*K
for i in range(K):
  D[i]=int(input())
  a=list(map(int, input().split(' ')))
  for index in a:
    A[index-1]=A[index-1]+1
    
print(A.count(0))