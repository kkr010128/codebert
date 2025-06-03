n = int(input())
for i in range(n):
    nums = sorted(map(int, input().split()))
    print("YES" if nums[2]**2 == nums[1]**2 + nums[0]**2 else "NO")