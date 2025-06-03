n = int(input())
d = list(map(int, input().split()))
ans = float('inf')
fh = 0
lh = sum(d)
for i in range(0,n):
  fh += d[i]
  lh -= d[i]
  ans = min(abs(fh - lh), ans)
print(ans)