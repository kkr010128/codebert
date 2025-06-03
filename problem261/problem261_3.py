import sys
import time
import math
def inpl():
    return list(map(int, input().split()))
st = time.perf_counter()
# ------------------------------

S = input()
T = S[::-1]
ans = 0
for i in range(len(S)//2):
	if S[i] != T[i]:
		ans += 1
print(ans)

# ------------------------------
ed = time.perf_counter()
print('time:', ed-st, file=sys.stderr)
