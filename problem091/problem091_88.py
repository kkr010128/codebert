from itertools import combinations
N = int(input())
nums = list(map(int,input().split()))
tcount = 0
numset = set(nums)
comb = combinations(numset,3)
for i in list(comb):
	a = i[0]
	b = i[1]
	c = i[2]
	if(a+b>c and b+c>a and a+c>b):
		tcount += nums.count(a)*nums.count(b)*nums.count(c)
print(tcount)
