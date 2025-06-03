import itertools

N, K = map(int, input().split())
d = []
A = []
for i in range(K):
    d.append(int(input()))
    A.append(list(map(int, input().split())))

A = list(itertools.chain.from_iterable(A))
ans = 0
for i in range(1, N + 1):
    if i in A:
        continue
    else:
        ans += 1

print(ans)