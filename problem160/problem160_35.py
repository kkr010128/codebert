from itertools import combinations_with_replacement
n, m, q = map(int, input().split())
s_l = []
for i in range(q):
    s = list(map(int, input().split()))
    s_l.append(s)

A = []
for v in combinations_with_replacement(range(1,m+1), n):
    A.append(v)

ans = 0
for a in A:
    cnt = 0
    for i in range(q):
        if a[s_l[i][1] - 1] - a[s_l[i][0] - 1] == s_l[i][2]:
            cnt += s_l[i][3]
    ans = max(ans, cnt)

print(ans)