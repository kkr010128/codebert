n = int(input())
a = list(map(int, input().split()))
s, l = sum(a), 0
for i in range(n):
  l += a[i]
  if l>= s/2:
    ans = min([abs(l-a[i]-sum(a[i:])),abs(l-sum(a[i+1:]))])
    print(round(ans))
    break