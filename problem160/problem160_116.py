import itertools

N, M, Q = map(int, input().split())
A = [list(map(int, input().split())) for i in range(Q)]
a_list = []
ans = 0

for i in itertools.combinations_with_replacement(range(1,M+1),N):
    ans2 = 0
    for t in A:
        if i[t[1]-1] - i[t[0]-1] == t[2]:
            ans2 += t[3]

    ans = max(ans,ans2)

print(ans)
