import itertools

n = int(input())
l = list(map(int, input().split()))

c = list(itertools.combinations(l, 3))
ans = 0
for i in c:
    j = sorted(i)
    if j[0] != j[1] != j[2] != j[0]:
        if j[2] < j[0]+j[1]:
            ans += 1
print(ans)
