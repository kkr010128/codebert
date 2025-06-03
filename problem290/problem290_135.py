import sys
input = sys.stdin.buffer.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
F = list(map(int, input().split()))

A = sorted(A)
F = sorted(F)[::-1]

left = -1
right = max(A) * max(F)

while left + 1 < right:
  mid = (left + right) // 2
  tmp = 0
  for i in range(N):
    a, f = A[i], F[i]
    if a * f > mid:
      tmp += -(-(a * f - mid) // f)
  if tmp <= K:
    right = mid
  else:
    left = mid
    
print(right)