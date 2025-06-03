import itertools
N, K = map(int, input().split())
p = list(map(int, input().split()))

pos = [(p[i]+1)/2 for i in range(N)]

pos_acum = list(itertools.accumulate(pos))

ans = pos_acum[K-1]
for i in range(N-K):
    ans = max(ans, pos_acum[K+i]-pos_acum[i])
print(ans)