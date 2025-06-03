N = int(raw_input())
nums = []

for i in range(N):
    nums.append(int(raw_input()))

m = -1000000000000000000000000
minvalue = nums[0]

for i in range(1, len(nums)):
    minvalue = min(minvalue, nums[i-1])
    value = nums[i] - minvalue
    if m <= value:
        m = value

print(m)