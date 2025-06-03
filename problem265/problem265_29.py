import sys
import time
import math
def inpl():
    return list(map(int, input().split()))
st = time.perf_counter()
# ------------------------------

N = int(input())
ls = [0] * 50505
for i in range(len(ls)):
	ls[i] = int(i * 1.08)
for i in range(N, 0, -1):
	if ls[i] == N:
		print(i)
		sys.exit()
print(':(')

# ------------------------------
ed = time.perf_counter()
print('time:', ed-st, file=sys.stderr)
