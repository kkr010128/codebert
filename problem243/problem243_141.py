N = int(input())
s, t = [], []
for i in range(N):
  s_i, t_i = input().split(" ")
  t_i = int(t_i)
  s.append(s_i)
  t.append(t_i)
X = input()

idx = 0
while idx < N:
  if s[idx] == X:
    idx += 1
    break
  idx += 1

ans = 0
for i in range(idx, N):
  ans += t[i]
print(ans)