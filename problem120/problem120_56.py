N,K = map(int, input().split())
P = list(map(int, input().split()))
P.sort()
plist = P[0:K]
a = 0
for p in plist:
	a+=p
print(a)