k,n = map(int,input().split())
a = list(map(int,input().split()))
b = []

for i in range(1,n):
  b.append(a[i] - a[i-1])
b.append(k - a[n-1] + a[0])
b = sorted(b)

print(sum(b[:-1]))
