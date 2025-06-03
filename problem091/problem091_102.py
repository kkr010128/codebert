import itertools

n = int(input())
L = list(map(int, input().split()))

L.sort(reverse = True)
li = list(itertools.combinations(L, 3))

ans = 0
for v in li:
    if v[0] != v[1] and v[1] != v[2] and v[0] - v[1] < v[2]:
        ans += 1
print(ans)
