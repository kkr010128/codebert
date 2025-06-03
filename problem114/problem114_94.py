D = int(input())
C = list(map(int, input().split()))
s = list()
for i in range(D):
  s1 = list(map(int, input().split()))
  s.append(s1)
t = list()
for i in range(D):
  N = int(input())
  t.append(N-1)
done = [0] * 26

ans = 0
for d in range(1, D+1):
  td = t[d-1]
  done[td] = d
  ans += s[d-1][td]
  for i in range(26):
    ans -= C[i]*(d-done[i])
  print(ans)