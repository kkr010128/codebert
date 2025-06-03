import itertools

n = int(input())
tastes = list(map(int, input().split()))

ans_lists = []
for v in itertools.combinations(tastes, 2):
    cure = v[0]*v[1]
    ans_lists.append(cure)

ans = 0
for i in ans_lists:
    ans += i
print(ans)