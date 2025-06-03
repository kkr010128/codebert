n = int(input())
min = 2000000
max = -2000000

nums = list(map(int,input().split()))
sum = 0

for i in range(n):
	sum += nums[i]
	
	if nums[i] < min:
		min = nums[i]
	if nums[i] > max:
		max = nums[i]

print(min,max,sum)