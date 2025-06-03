n = int(input())
a = list(map(int,input().split()))
a_max = max(a)

ans = 0
for i in range(1, n):
  if a[i - 1] > a[i]:
    ans += a[i - 1] - a[i]
    a[i] = a[i - 1]

print(ans)