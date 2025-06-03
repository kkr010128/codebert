n = int(input())

nums = list(map(int, input().split()))

ans = 0
for idx in range(1, n):
    if nums[idx] - nums[idx-1] < 0:
        ans += abs(nums[idx] - nums[idx-1])
        nums[idx] = nums[idx-1]

print(ans)