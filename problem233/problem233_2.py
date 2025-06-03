N=int(input())
L=list(map(int,input().split()))
ans=1
M=L[0]
for i in range(1,N):
  if M>=L[i]:
    M=L[i]
    ans+=1
  else:
    continue
print(ans)