n = int(input())
A = [0] * (n + 1)
for i in range(1, n + 1):
  for j in range(i, n + 1, i):
    A[j] += 1
print(sum(i * A[i] for i in range(1, n + 1)))