n = input()
lis = map(int, raw_input().split())
mn = lis[0]
mx = lis[0]
for t in lis:
	if mn > t:
		mn = t
	if mx < t:
		mx = t
print mn, mx, sum(lis)