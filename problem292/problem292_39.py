from itertools import combinations

n = int(input())
d = list(map(int, input().split()))
ans = 0
sum = sum(d)
for i in d:
    sum -= i
    ans += i*sum
print(ans)