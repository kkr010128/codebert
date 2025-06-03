N,M=map(int,input().split())
ans=[]
if N%2==1:
  for i in range(M):
    ans.append([i+1,N-i])
else:
  for i in range(M//2):
    ans.append([i+1,2*M-i+1])
  for j in range(M-M//2):
    ans.append([j+M//2+1,2*M-M//2-j])
for k in ans:
  print(*k,sep=' ')