S=input()
N=len(S)+1
LEFT=[0]
RIGHT=[0]
left=0
right=0
for i in range(N-1):
  if S[i]==">":
    left=0
  else:
    left+=1
  LEFT+=[left]
for i in range(N-2,-1,-1):
  if S[i]=="<":
    right=0
  else:
    right+=1
  RIGHT+=[right]
ans=0  
for i in range(N):  
  ans+=max(LEFT[i],RIGHT[N-1-i])
print(ans)  