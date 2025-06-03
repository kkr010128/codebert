S = list(input())
N = len(S)
K = int(input())
old = S[0]
a = 0
c = 1
for i in range(1,N):
  if S[i] == old:
    c += 1
  else:
    a += c // 2
    old = S[i]
    c = 1
b = 0
a += c // 2
for i in range(N):
  if S[i] == old:
      b += 1
  else:
    break
ans = a * K + ((b + c) // 2 - b // 2 - c // 2) * (K - 1)
if c == N:
  ans = N * K // 2
print(ans)