L, R, d = map(int, input().split())
a = 1
ans = 0
while a*d <= R:
  if a*d >= L:
    ans += 1
  a += 1
  
print(ans)