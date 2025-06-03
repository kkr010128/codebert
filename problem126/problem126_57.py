nums = list(map(int, input().split()))
for i in nums:
  if i == 0:
    print(nums.index(i) + 1)
    break