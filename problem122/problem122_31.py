from collections import Counter

n = int(input())
A = [int(i) for i in input().split()]
all = sum(A)

Q = int(input())
bc = [[int(i) for i in input().split()] for _ in range(Q)]

nums = {i:0 for i in range(1, 10 ** 5 + 1)}
for a in A:
    nums[a] += 1

for i in range(Q):
    #print(nums)
    b, c = bc[i][0], bc[i][1]
    if b in nums.keys(): all += (c - b) * nums[b]
    print(all)

    nums[c] += nums[b]
    nums[b] = 0