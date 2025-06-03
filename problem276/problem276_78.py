from itertools import accumulate
n = int(input())
a = list(map(int, input().split()))
ac = list(accumulate(a))
total = ac[-1]
ans = float('inf')
for i in range(n-1):
    l, r = ac[i], total - ac[i]
    ans = min(ans, abs(l-r))
print(ans)