n = int(input())
A = list(map(int, input().split()))

from collections import defaultdict
dic = defaultdict(int)

ans = 0
for i in range(n):
  if i - A[i] in dic:
    ans += dic[i-A[i]]
  dic[i+A[i]] += 1
print(ans)

