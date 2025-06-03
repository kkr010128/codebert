s = input()
t = input()
n = len(s)
ans = n
for i in range(n):
  if s[i] == t[i]:
    ans -= 1
print(ans)