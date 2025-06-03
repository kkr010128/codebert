a, b, c, d = map(int, input().split())
x = [a, min(a+1, b), max(a, b-1), b]
y = [c, min(c+1, d), max(c, d-1), d]

ans = -int(1e19)
for i in x:
  for j in y:
    ans = max(ans, i*j)
print(ans)