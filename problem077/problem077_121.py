nums = input().split()
ab = [int(nums[0]), int(nums[1])]
cd = [int(nums[2]), int(nums[3])]

res = []

for i in ab:
  for j in cd:
    tmp = i * j
    res.append(tmp)
    
print(max(res))