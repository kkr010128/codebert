K,N=map(int,input().split())
A=list(map(int,input().split()))
B=[K-A[N-1]+A[0]]
for x in range(N-1):
  B.append(A[x+1]-A[x])
ans=sum(B)-max(B)
print(ans)
