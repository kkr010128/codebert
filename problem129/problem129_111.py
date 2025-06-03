n = int(input())
arr = list(map(int,input().split()))

nums = list(set(arr))
nums.sort()
last = nums[-1]
from collections import Counter
arr = Counter(arr)
ans = 0

for i in nums:
    if arr[i] == 1:
        ans += 1
    for j in range(last//i+1):
        del arr[i*j]

print(ans)