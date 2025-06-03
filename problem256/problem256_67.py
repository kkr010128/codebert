def gcd(_a, _b):
	if _a%_b==0:return _b
	else:return gcd(_b, _a%_b)

A, B=map(int, input().split())
print(A*B//gcd(A, B))
