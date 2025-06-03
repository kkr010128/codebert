# D - Moving Piece

n, k = map(int, input().split())
p = list(map(int, input().split()))
c = list(map(int, input().split()))
assert len(p) == len(c) == n

visited = [False] * n
scc = []
for i in range(n):
    if not visited[i]:
        scc.append([])
        j = i
        while not visited[j]:
            visited[j] = True
            scc[-1].append(j)
            j = p[j] - 1

n_scc = len(scc)
subsum = [[0] for i in range(n_scc)]
for i in range(n_scc):
    for j in scc[i]:
        subsum[i].append(subsum[i][-1] + c[j])
    for j in scc[i]:
        subsum[i].append(subsum[i][-1] + c[j])

def lister(k):
    for i in range(n_scc):
        l = len(scc[i])
        loop_score = max(0, subsum[i][l])
        for kk in range(1, min(k, l) + 1):
            base = loop_score * ((k - kk) // l)
            for j in range(kk, l + kk + 1):
                yield base + subsum[i][j] - subsum[i][j - kk]

print(max(lister(k)))
