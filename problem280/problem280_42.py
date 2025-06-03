import itertools

n=int(input())
ab = []
for _ in range(n):
    a, b = (int(x) for x in input().split())
    ab.append([a, b])

memo = []
for i in range(n):
    memo.append(i)

ans = 0
count = 0
for v in itertools.permutations(memo, n):
    count += 1
    tmp_root = 0
    for i in range(1, n):
        tmp_root += ((ab[v[i-1]][0]-ab[v[i]][0])**2+(ab[v[i-1]][1]-ab[v[i]][1])**2)**0.5
    ans += tmp_root

print(ans/count)