n,k,s = map(int, raw_input().split())
r = [s] * k 

if s == 10 ** 9:
	for i in range(n - k):  r.append((10 ** 9) - 2)
else:
	for i in range(n - k):  r.append(s + 1)
for a in r: print a,
