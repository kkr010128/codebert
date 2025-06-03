from collections import Counter

N = int(input())
nums = list(map(int, input().split()))

A = [i + n for i, n in enumerate(nums, start=1)]
B = [j - n for j, n in enumerate(nums, start=1)]
BC = Counter(B)
answer = 0
for a in A:
  answer += BC[a]
print(answer)