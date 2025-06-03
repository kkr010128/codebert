n = int(input())

nums = []
nums = list(map(int, input().split()))
nums = sorted(nums, reverse=True)

cnt = 0

fir_num = nums[0]

del nums[0]

for i in range(n-2):
    fir_num += nums[int(i/2)]


print(fir_num)






