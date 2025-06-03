n = input()
A=[int(j) for j in input().split()]

nums = [0,0,0]
ans = 1
for a in A:
  ans = (ans*nums.count(a))%(10**9 +7)
  for i in range(len(nums)):
        if nums[i] == a:
            nums[i] = a+1
            break
          
print(ans)