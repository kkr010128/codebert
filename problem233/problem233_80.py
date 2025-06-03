n = int(input())
ps = [int(i) for i in input().split()]
now = ps[0]
cnt = 1
for p in ps:
	if p < now:
		cnt += 1
		now = p
print(cnt)