INF = 10**18

N, K, C = map(int, input().split())
S = input()

lt = [-INF for _ in range(K + 1)]
rt = [-INF for _ in range(K + 1)]

j = -1
for i in range(1, K + 1):
    while True:
        j += 1
        if S[j] == 'o' and j - lt[i - 1] > C:
            lt[i] = j
            break

j = -1
for i in range(1, K + 1):
    while True:
        j += 1
        if S[-1 - j] == 'o' and j - rt[i - 1] > C:
            rt[i] = j
            break

lt = lt[1:]
rt = rt[1:]
rt = [N - x - 1 for x in rt]
rt = rt[::-1]

res = []

for i in range(K):
    if lt[i] == rt[i]:
        res.append(lt[i] + 1)

print('\n'.join(map(str, res)))
