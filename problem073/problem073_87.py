N = int(input())

count = 0
for A in range(1, N):
  N_ = (N - 1) // A
  count += N_

print(count)