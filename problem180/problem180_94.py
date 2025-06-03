def manipulate(x, k):
	return abs(x - k)

n, k = list(map(int, input().split()))
n = n % k

while n > k / 2:	
	n = manipulate(n, k)
	
print(n)