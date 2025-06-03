nums = [int(e) for e in input().split()]

if (nums[2]+nums[4])<=nums[0] and (nums[3]+nums[4])<=nums[1] and (nums[2]-nums[4])>=0 and (nums[3]-nums[4])>=0:
    print("Yes")
else:
    print("No")
