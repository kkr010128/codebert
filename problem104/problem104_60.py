l,r,d = [int(x) for x in input().split()]
nums = [int(x) for x in range(l,r+1)]
ans = []

for i in range(len(nums)):
      if nums[i]%d == 0:
            ans.append(nums[i])

print(len(ans))