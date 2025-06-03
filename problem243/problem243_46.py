N = int(input())
s, t = [0]*N, [0]*N
for i in range(N):
  s[i], t[i] = input().split()
X = input()

ans = 0
flag = False
for i in range(N):
  if flag:
    ans += int(t[i])
  if s[i] == X:
    flag = True

print(ans)