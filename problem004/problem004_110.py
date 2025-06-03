# -*- config: utf-8 -*-
if __name__ == '__main__':
	for i in range(int(raw_input())):
		nums = map(lambda x:x**2,map(int,raw_input().split()))
		nums.sort()
		if nums[0]+nums[1] == nums[2]:
			print "YES"
		else :
			print "NO"