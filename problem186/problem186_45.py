K, N = map(int, input().split())
nums = list(map(int, input().split()))

before = 0
max_n = 0
for num in nums:
  dist = num - before
  max_n = max(max_n, dist)
  before = num
max_n = max(max_n, K-nums[-1]+nums[0])
print(K-max_n)