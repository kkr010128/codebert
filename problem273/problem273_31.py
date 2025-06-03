from collections import defaultdict

n, k = map(int, input().split())

seq = list(map(int, input().split()))

count = defaultdict(int)
count[0] = 1

prefix = [0]*(n+1)
ans = 0

for i in range(n):
  pre = prefix[i+1] = (prefix[i] + seq[i] - 1)%k
  
  if i >= k - 1:
    count[prefix[i - k + 1]] -= 1
  ans += count[pre]
  count[pre] += 1
print(ans)