n = int(input())
d = list(map(int,input().split()))
ans = 0
for i in range(n):
  ans += d[i] * (sum(d) - d[i])
print(ans // 2)