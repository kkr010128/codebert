n = int(input())
A = list(map(int, input().split()))

ret = 1000
prev = A[0]
for i in range(1, n):
  if A[i] - prev > 0:
    ret = A[i] * (ret // prev) + ret % prev
  if A[i] != prev:
    prev = A[i]

print(ret)