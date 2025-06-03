from sys import stdin
input = stdin.buffer.readline

n, k = map(int, input().split())
*a, = map(int, input().split())
for i in range(k, n):
	if a[i] > a[i - k]:
		print('Yes')
	else:
		print('No')
