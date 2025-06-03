S=list(str(input()))
a=[]
b=[]

count = 1
direction=S[0]
for i in range(1,len(S)):
  if S[i]== direction:
    count += 1
  else:
    a.append(S[i-1])
    b.append(count)
    direction=S[i]
    count=1
a.append(S[-1])
b.append(count)
m=max(b)+1
dp=[0]*m
for i in range(1,m):
  dp[i] += dp[i-1]+i
ans=0
for i in range(1,len(a)):
  if a[i-1]=='<' and a[i]=='>':
    ans+=dp[max(b[i-1],b[i])] + dp[min(b[i-1],b[i])-1]
  
if a[0]=='>':
  ans+=dp[b[0]]
if a[-1]=='<':
  ans+=dp[b[-1]]
print(ans)