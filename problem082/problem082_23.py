s = input()
t = input()

n = len(s)
m = len(t)

ans = float("inf")
for i in range(n-m+1):
  p = m
  for j in range(m):
    if s[i+j] == t[j]: p -= 1
  if p < ans: ans = p
print(ans)