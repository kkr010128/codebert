N = int(input())
A = list(map(int, input().split()))

kabu = 0
yen = 1000

for i in range(N-1):
  if A[i] < A[i+1]:
    buy = yen//A[i]
    kabu += buy
    yen -= buy * A[i]
  elif A[i] > A[i+1]:
    yen += kabu * A[i]
    kabu = 0

if kabu > 0:
  yen += A[-1] * kabu
  kabu = 0

print(yen)