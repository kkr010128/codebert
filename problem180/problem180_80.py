# C Replacing Integer

N, K = map(int, input().split())

while N >= K:
  N = N % K

frag = 0
while frag == 0:
  cand = abs(N - K)
  if cand < N:
    N = cand
  else:
    frag = 1
print(N)