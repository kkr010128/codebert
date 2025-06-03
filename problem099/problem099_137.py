n, k = map(int, input().split())
a = list(map(int, input().split()))
low = 0
top = max(a) + 1

while top - low > 1:
  mid = (top + low) // 2
  cnt = 0
  for i in range(n):
    if a[i] % mid == 0:
      cnt += (a[i] // mid) - 1
    else:
      cnt += a[i] // mid
  if cnt <= k:
    top = mid
  else:
    low = mid
print(top)
