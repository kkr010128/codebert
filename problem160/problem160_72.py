# https://atcoder.jp/contests/abc165/tasks/abc165_c

from itertools import combinations_with_replacement

N, M, Q = map(int, input().split())
data = []
for _ in range(Q):
    data.append(list(map(int, input().split())))

res = []
for A in combinations_with_replacement(range(1,M+1), N):
    score = 0
    for i in range(Q):
        a,b,c,d = data[i]
        if A[b-1] - A[a-1] == c:
            score += d
    res.append(score)

print(max(res))