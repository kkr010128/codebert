N = int(input())
l = []
for _ in range(N):
  s, t = input().split()
  t = int(t)
  l.append([s, t])
X = input()

ans = 0
found = False
for s in l:
  if found:
    ans += s[1]
    continue
  if s[0] == X:
    found = True
    
print(ans)