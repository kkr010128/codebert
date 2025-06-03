n, k = map(int, input().split())
arr = list(map(int, input().split()))
expected = []
cumsum = []
for x in arr:
	sum = (x * (x + 1)) // 2
	ex = sum / x
	expected.append(ex)

sum = 0
maxi = 0
taken = 0
bad = 0
for x in expected:
	sum += x
	taken += 1
	if taken == k:
		 maxi = max(maxi, sum)
	elif taken > k:
		sum -= expected[bad]
		bad += 1
		maxi = max(maxi, sum)
print(maxi)