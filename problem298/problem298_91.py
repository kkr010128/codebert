n,k = map(int, input().split())
H = list(map(int, input().split()))
ans = 0
for i in range(n):
  if H[i] >= k:
    ans += 1
  else:
    pass
print(ans)