n, k = map(int, input().split())
nums = list(map(int, input().split()))

# (sums[j] - sums[i]) % K = j - i
# (sums[j] - j) % K  = (sums[i] - i) % K
# 1, 4, 2, 3, 5
# 0, 1, 5, 7, 10, 15
# 0, 0, 3, 0, 2, 2

sums = [0]
for x in nums:
  sums.append(sums[-1] + x)

a = [(sums[i] - i) % k for i in range(len(sums))]

res = 0
memo = {}
i = 0 
for j in range(len(a)):
  memo[a[j]] = memo.get(a[j], 0) + 1
  if j - i + 1 > k:
    memo[a[i]] -= 1
    i += 1
  res += memo[a[j]] - 1
print(res)