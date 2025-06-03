import sys
def input():
	return sys.stdin.buffer.readline()[:-1]

n = int(input())
d = [list(map(int, input().split())) for _ in range(n)]
ans1 = max(x[0] + x[1] for x in d) - min(x[0] + x[1] for x in d)
ans2 = max(x[0] - x[1] for x in d) - min(x[0] - x[1] for x in d)
print(max(ans1, ans2))