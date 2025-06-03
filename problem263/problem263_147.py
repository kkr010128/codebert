n = int(input())
a = list(map(int,input().split()))
maxketa = max([len(bin(a[i])) for i in range(n)])-2
mod = 10**9+7
ans = 0
for i in range(maxketa):
	ones = 0
	for j in range(n):
		if (a[j] >> i) & 1:
			ones += 1
	ans = (ans + (n-ones)*ones*(2**i)) % mod
 
print(ans)