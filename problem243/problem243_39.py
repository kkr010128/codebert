N = int(input())
ls = []
for i in range(N):
  s = input().split()
  ls.append(s)
X = input()
ans = 0
mode = 0
for i in range(N):
  if ls[i][0] == X:
    mode = 1
  else:
    if mode == 1:
      ans += int(ls[i][1])
print(ans)