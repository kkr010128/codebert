MOD = 10**9+7
n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
#print(a)
kai = [1]
gai = []
for i in range(n):
	j = (kai[i] * (i+1)) % MOD
	kai.append(j)
for i in range(n+1):
	j = kai[i]
	l = pow(j, MOD-2, MOD)
	gai.append(l)
#print(kai)
#print(gai)

ans = 0
for i in range(n):
	if i <= (n-k):
		#print('xあり')
		x = (a[i] * kai[n-i-1] * gai[n-i-k] * gai[k-1]) % MOD
	else:
		x = 0
	#print('xha', x)

	if i >= (k-1):
		#print('yあり')
		y = (a[i] * kai[i] * gai[i-k+1] * gai[k-1]) % MOD
	else:
		y = 0
	#print('yha', y)

	ans = (ans + y - x) % MOD
	#print(ans)

print(ans)