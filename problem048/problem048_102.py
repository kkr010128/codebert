n = int(input())
nums = [int(i) for i in input().split(' ')]
nums_sorted = sorted(nums)
min = nums_sorted[0]
max = nums_sorted[n - 1]
print(min, max, sum(nums_sorted))
