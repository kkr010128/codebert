def divide(a, b):
	if a < b:
		return divide(b, a)
	if b == 0:
		return a
	return divide(b, a%b)
	
nums=list(map(int,input().split()))

ans = divide(nums[0], nums[1])

print(ans)
