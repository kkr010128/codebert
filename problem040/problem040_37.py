
nums = map(int, raw_input().split())

for i in range(2):
    for j in range(2-i):
        if nums[j] > nums[j+1]:
            temp      = nums[j]
            nums[j]   = nums[j+1]
            nums[j+1] = temp

print(str(nums[0]) + " " + str(nums[1]) + " " + str(nums[2]))