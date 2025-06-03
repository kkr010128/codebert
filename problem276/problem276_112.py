# https://atcoder.jp/contests/ddcc2020-qual/tasks/ddcc2020_qual_b

n = int(input())
nums = [int(i) for i in input().split()]
for i in range(n - 1):
    nums[i + 1] += nums[i]

ans = float('inf')
for i in range(n - 1):
    d = abs(nums[-1] - nums[i] * 2)
    ans = min(ans, d)
print(ans)