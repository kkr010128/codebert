N=int(input())
P=list(map(int,input().split()))

m_v=N+1
ans=0
for i in range(N):
  m_v=min(m_v,P[i])
  if m_v==P[i]:
    ans+=1

print(ans)
