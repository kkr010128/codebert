n = int(input())
a = [int(x) for x in input().split()]
res = 0
for i in range(1,n):
  if a[i] > a[i-1]:
    continue
  else:
    res += a[i-1] - a[i]
    a[i] = a[i-1]
print(res)