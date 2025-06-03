n,k,s = map(int,input().split())
ans = []
for i in range(k):
  ans.append(str(s))
  
for j in range(n-k):
  if s != 1000000000:
    ans.append(str(s+1))
  else:
    ans.append(str(s-1))
print(' '.join(ans))