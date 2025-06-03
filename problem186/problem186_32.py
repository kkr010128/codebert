k,n = map(int, input().split())
a = list(map(int, input().split()))
l = [a[n-1]-a[0]]
for i in range(n-1):
  l.append(k-a[i+1]+a[i])
print(min(l))