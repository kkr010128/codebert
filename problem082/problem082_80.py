s = input()
t = input()
ans = len(t)
c = 0
for i in range(len(s)-len(t)+1):
  c = 0
  for j in range(len(t)):
    if s[i+j] != t[j]:
      c += 1
  if ans > c:
    ans = c
print(ans)

