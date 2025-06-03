n,k = map(int, input().split())
a = list(map(int, input().split()))

l = [0]*(n-k+1)
l[0] = sum(a[:k])
for i in range(k,n): l[i-k+1] = l[i-k] + a[i] - a[i-k]
for i in range(1,n-k+1):
  if l[i-1] < l[i]: print("Yes")
  else: print("No")