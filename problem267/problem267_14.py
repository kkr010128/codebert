N = int(input())
S = input()
ans = 0
for i in range(10):
    for j in range(10):
        for k in range(10):
            nums = [str(x) for x in [i, j, k]]
            for s in S:
                if s == nums[0]:
                    nums = nums[1:]
                    if len(nums) == 0:
                        ans += 1
                        break
print(ans)
