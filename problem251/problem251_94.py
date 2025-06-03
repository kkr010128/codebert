N, K = map(int, input().split())
ls1 = list(map(int, input().split()))
d = dict()
ls2 = ['r', 's', 'p']
for x, y in zip(ls1, ls2):
    d[y] = x
T = input()

S = T.translate(str.maketrans({'r': 'p', 's': 'r', 'p': 's'}))
ans = 0
for i in range(K):
    cur = ''
    for j in range(i, N, K):
        if cur != S[j]:
            ans += d[S[j]]
            cur = S[j]
        else:
            cur = ''
print(ans)