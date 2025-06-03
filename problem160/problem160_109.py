from itertools import combinations_with_replacement
N, M, Q = map(int, input().split())
Ques = [ list(map(int, input().split())) for _ in range(Q) ]

Nums = [ i for i in range(M) ]
ans = -1
for v in combinations_with_replacement(Nums, N):
    cnt = 0
    for que in Ques:
        if v[que[1]-1]-v[que[0]-1] == que[2]: cnt += que[3]
    ans = max(ans, cnt)
print(ans)