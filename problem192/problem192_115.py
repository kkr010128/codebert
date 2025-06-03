N = int(input())
A = list(map(int, input().split()))

nums = [0]*N

for val in A:
    nums[val-1] += 1

choices = 0
for num in nums:
    choices += int(num * (num - 1) / 2)

for val in A:
    print(choices - nums[val - 1] + 1)