#Eans

import sys, math, itertools, collections, bisect
mans = float('inf')
mod = 10 **9 +7
ans = 0
count = 0
pro = 0

N, M = map(int, input().split())
A = sorted(map(int, input().split()))
B = [0] + A[:]
for i in range(N):
  B [i+1] += B[i]

#print('A', A)
#print('B', B)
def solve_binary(mid):
  tmp = 0
  for i, ai in enumerate(A):
    tmp += N - bisect.bisect_left(A, mid-ai)
    #bisect.bisect_left(A, mid-ai)はaiに固定した時の、もう片方の最小の値のインデックス
    #tmpは、aiに固定した時のありうる個数（M)
  return tmp >= M

def binary_search(N):
  ok = 0
  ng = N
  while abs(ok - ng ) > 1:
    mid = (ok + ng) // 2
    if solve_binary(mid):
      ok = mid
    else:
      ng = mid
  return ok


binresult = binary_search(2*10**5+1)
#Xを二分探索で得る
#binresult=ok
#print(binresult)
for i, ai in enumerate(A):
  ans += ai*(N - bisect.bisect_left(A, binresult-ai)) + B[N] - B[bisect.bisect_left(A, binresult-ai)]
  #print(ans, '=', ai, '*', N-bisect.bisect_left(A, binresult-ai), '+', B[N], '-', B[bisect.bisect_left(A, binresult-ai
  count += N - bisect.bisect_left(A, binresult-ai)
ans -= binresult * (count-M)
print(ans)