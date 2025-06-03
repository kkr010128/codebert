from collections import defaultdict
"""
N 以下の全ての整数に対して, (先頭, 末尾) を数える.
(先頭, 末尾), (末尾, 先頭)の組は, 独立しているので掛け算で求められる.
"""
n = int(input())
ansl = defaultdict(lambda: 0)
for i in range(1,n+1):
	sentou = int(str(i)[0])
	ushiro = int(str(i)[-1])
	ansl[(sentou, ushiro)] += 1
ans = 0
for i in range(1, 10):
	for j in range(1, 10):
		ans += ansl[(i, j)]*ansl[(j, i)]
print(ans)