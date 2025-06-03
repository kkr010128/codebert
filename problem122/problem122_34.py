n = int(input())
arr = list(map(int, input().split()))
s = sum(arr)
d = dict()
for i in arr:
	if (i not in d):
		d[i] = 1
	else:
		d[i] += 1
q = int(input())
for i in range(q):
	b, c = map(int, input().split())
	if (b in d):
		s -= b * d[b]
		s += c * d[b]
		if (c not in d):
			d[c] = d[b]
		else:
			d[c] += d[b]
		d.pop(b)
	print(s)