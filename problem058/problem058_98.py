from itertools import combinations as comb
def get_ans(m, n):
	ans = 0
	for nums in comb(list(range(1, min(m+1,n-2))), 3):
		if sum(nums) == n:
			ans += 1
	print(ans)
	
while True:
	m, n = (int(x) for x in input().split())
	if m==0 and n==0:
		quit()
	get_ans(m, n)
