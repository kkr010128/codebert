N = int(input())
A = list(map(int, input().split()))
step = 0
for i in range(N - 1):
  step += max(0, A[i] - A[i + 1])
  A[i + 1] += max(0, A[i] - A[i + 1])
print(step)
