import itertools
n = int(input())
d = list(map(int, input().split()))
lst = list(itertools.combinations(d, 2))

ans = 0
for i in lst:
    a = i[0] * i[1]
    ans += a
print(ans)
