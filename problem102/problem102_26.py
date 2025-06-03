n,k = map(int,input().split())
a = list(map(int,input().split()))
ans = []
for i in range(k,n):
  ans.append(a[i] - a[i-k])
for j in ans:
  if j > 0:
    print('Yes')
  else:
    print('No')