import sys
import time
import math
def inpl():
    return list(map(int, input().split()))
st = time.perf_counter()
# ------------------------------

N = int(input())
d = inpl()
ans = 0
for i in range(N-1):
	for j in range(i+1, N):
		ans += d[i] * d[j]
print(ans)
	

# ------------------------------
ed = time.perf_counter()
print('time:', ed-st, file=sys.stderr)
