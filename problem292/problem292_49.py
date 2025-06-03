import itertools


N = int(input())
D = [int(x) for x in input().split()]

ans = 0
for v in itertools.combinations(D,2):
    ans += v[0]*v[1]

print(ans)
