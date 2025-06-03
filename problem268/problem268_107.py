n = int(input())
A = list(map(int, input().split()))

from collections import defaultdict
dic = defaultdict(int)
dic[0] = 3
ans = 1

mod = 1000000007
for a in A:
  ans *= dic[a]
  ans = ans % mod
  dic[a] -= 1
  dic[a+1] += 1
print(ans)