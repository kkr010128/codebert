N=int(input())
A=list(map(int, input().split()))
m=N+1
ct=0
for i in range(N):
  if A[i]<m:
    ct+=1
    m=A[i]
print(ct)