line = int(input())
nums = []
for n in range(line):
    nums.append(int(input()))

# res = nums[1] - nums[0]
# for i in range(line):
#     for j in range(i+1, line):
#         dif = nums[j] - nums[i]
#         res = dif if dif > res else res
maxd = nums[1] - nums[0]
minv = nums[0]

for j in range(1, line):
    maxd = max(maxd, nums[j] - minv)
    minv = min(minv, nums[j])


print(maxd)