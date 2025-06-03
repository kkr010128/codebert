n, k = map(int, input().split())
a = list(map(int, input().split()))
f = list(map(int, input().split()))
a.sort()
f.sort()
high = max(a)*max(f)
low = 0
while high > low:
  mid = (high+low)//2
  b = 0
  for i in range(n):
    b += max(a[i]-mid//f[n-i-1],0)
  if b > k:
    low = mid + (low==mid)
  else:
    high = mid - (high==mid)
mid = (high+low)//2
print(mid)