N = int(input())

def cnt(n):
  c = 0
  for i in range(1, N+1):
    n = N // i
    j  = i * n
    c += (i + j) * n // 2
  return c

print(cnt(N))