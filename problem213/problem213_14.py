def rally(arr):
	p = max(arr)
	summ = 0
	best = float('inf')
	for i in range(1, p+1):
		summ = 0
		for j in arr:
			summ += (j - i) ** 2
		best = min(best, summ)
	return best
n = int(input())
arr = list(map(int, input().split()))
print(rally(arr))