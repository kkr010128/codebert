N, K = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))

seen = []
roots = []
candidates = []

for i in range(N):
    if i+1 in seen:
        continue
    root = [i+1]
    seen.append(i+1)
    to = P[i]
    while(root[0] != to):
        root.append(to)
        seen.append(to)
        to = P[to-1]
    roots.append(root)
for root in roots:
    length = len(root)
    eachMoveBests = [None] * length
    for i in range(length):
        score = 0
        to = P[root[i]-1]
        for j in range(len(root)):
            score += C[to-1]
            to = P[to-1]
            if eachMoveBests[j] == None or score > eachMoveBests[j]:
                eachMoveBests[j] = score
    # 周回スコア
    aroundScore = eachMoveBests[len(eachMoveBests)-1]
    if length < K and aroundScore > 0:
        for i in range(len(eachMoveBests)):
            if K-i-1 % length == 0:
                candidates.append(aroundScore * ((K-i-1) // length))
            else:
                candidates.append(aroundScore * ((K-i-1) // length) + eachMoveBests[i])
    else:
        candidates.append(max(eachMoveBests[:K]))

print(max(candidates))
