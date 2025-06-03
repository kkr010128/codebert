import itertools

n=int(input())
ab = []
for _ in range(n):
    a, b = (int(x) for x in input().split())
    ab.append([a, b])

narabi = [0+i for i in range(n)]

ans = 0
count = 0
for v in itertools.permutations(narabi, n):
    count += 1
    tmp_len = 0
    for i in range(1,n):
        x, y = abs(ab[v[i-1]][0]-ab[v[i]][0])**2, abs(ab[v[i-1]][1]-ab[v[i]][1])**2
        tmp_len += (x + y)**0.5
    ans += tmp_len

print(ans/count)