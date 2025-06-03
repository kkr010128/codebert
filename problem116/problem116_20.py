s = input()
t = input()
ans = 0
for c, d in zip(s, t):
  if c != d:
    ans += 1
print(ans)