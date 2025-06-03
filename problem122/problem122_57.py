N = int(input())
M = 10 ** 5 + 1
A = list(map(int, input().split()))
A2 = [0 for i in range(M)]
for a in A:
  A2[a] += 1
ans = sum(A)
Q = int(input())
for j in range(Q):
  b, c = map(int, input().split())
  ans = ans + (c - b) * A2[b]
  A2[c] += A2[b]
  A2[b] = 0
  print(ans)