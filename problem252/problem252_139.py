from bisect import bisect_left
from itertools import accumulate

N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))

Acum = [0] + list(accumulate(A))

left = 0
right = max(A) * 2 + 1

while left + 1 < right:
  mid = (left + right) // 2
  tmp = 0
  for i in range(N):
    bi = bisect_left(A, mid - A[i])
    tmp += N - bi
  if tmp <= M:
    right = mid
  else:
    left = mid

cnt = 0
answer = 0
for i in range(N):
  bi = bisect_left(A, right - A[i])
  cnt += N - bi
  answer += Acum[N] - Acum[bi] + A[i] * (N - bi)

print(answer + (M - cnt) * left)