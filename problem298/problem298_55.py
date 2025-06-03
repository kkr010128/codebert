n, k = map(int, input().rstrip().split())
h = [int(v) for v in input().rstrip().split()]
h.sort()
r = 0
for i in range(len(h)):
	if k <= h[i]:
		r = len(h) - i
		break

print(r)
