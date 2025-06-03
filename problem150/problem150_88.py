N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))
B = [-1 for i in range(N+1)]
B[1] = 0
n = 1
m = 0
while 1:
  n = A[n]
  m += 1
  if m == K:
    print(n)
    break
  if B[n] == -1:
    B[n] = m
  else:
    a = (K - m) % (m - B[n])
    for i in range(a):
      n = A[n]
    print(n)
    break