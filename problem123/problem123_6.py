N = int(input())
a = list(map(int, input().split()))

Xsum = 0
for i in a:
	Xsum = Xsum ^ i

ans = list()
for i in a:
	s = Xsum ^ i
#	print(s)
	ans.append(str(s))

print(' '.join(ans))