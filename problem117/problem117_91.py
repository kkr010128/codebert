n,m,k = map(int,input().split())
a = [0] + list(map(int,input().split()))
b = [0] + list(map(int,input().split()))
for i in range(1,n+1):
  a[i] += a[i-1]
for i in range(1,m+1):
  b[i] += b[i-1] 
ans,ai,bi = 0,0,0
for i in range(n+1):
  if a[i]<=k:
    ai = i
for j in range(m+1):
  if a[ai]+b[j]<=k:
    bi = j
ans = ai+bi
for i in range(ai):
  for j in range(bi,m+1):
    if a[ai-i-1]+b[j]>k:
      bi = j
      break
    else:
      ans = max(ans,ai-i-1+j)
print(ans)