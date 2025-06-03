N,M,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
sumA=[0]
for i in range(N):
  sumA.append(sumA[-1]+A[i])
sumB=[0]
for i in range(M):
  sumB.append(sumB[-1]+B[i])

ans=0
for i in range(N+1):
  k=K-sumA[i]
  if k<0:
    break
  left=0
  right=M
  while right>=left:
    mid=(right+left)//2
    if sumB[mid]>k:
      right=mid-1
    else:
      left=mid+1
  l=right
  ans=max(ans,i+l)
print(ans)