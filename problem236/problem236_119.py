H = int(input())
W = int(input())
N = int(input())

tmp1 = min(H, W)
tmp2 = max(H, W)

for i in range(tmp1):
  N = N - tmp2
  if N <= 0:
    print(i + 1)
    break