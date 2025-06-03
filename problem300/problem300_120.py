from math import gcd
A, B = map(int, input().split())
g = gcd(A, B)

plist = []

for i in range(2, int(g ** 0.5) + 1):
	if g % i == 0:
		plist.append(i)
		while(g % i == 0):
			g //= i
if g != 1:
	plist.append(g)

print(len(plist) + 1)