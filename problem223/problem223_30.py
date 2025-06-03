import sys
input = sys.stdin.readline

(n, k), s, res, sm = map(int, input().split()), list(map(lambda x: (int(x) + 1) / 2, input().split())), 0, 0
for i in range(n):
	if i < k: sm += s[i]
	else: sm += s[i]; sm -= s[i-k]
	res = max(res, sm)
print(f'{res:.10f}')
# print(f'{max([sum(s[i:i+k]) for i in range(n - k + 1)]):.10f}')