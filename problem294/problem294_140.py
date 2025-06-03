from bisect import bisect
from bisect import bisect_right
from bisect import bisect_left
 
N = int(input())
L = list(map(int, input().split()))
L.sort()
#print(L)
 
cnt = 0
for i in range(N):
  for j in range(i+1, N):
    s = L[i] + L[j]
    x = bisect_left(L, s)
    #print((L[i], L[j]), s, x)
    cnt += max(x - j - 1, 0)
print(cnt)