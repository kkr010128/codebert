N, M = map(int, input().split())
H = list(map(int, input().split()))
table = []
for i in range(N):
    table.append(set())
for i in range(M):
    Ai, Bi = map(lambda x: x - 1, map(int, input().split()))
    table[Ai].add(Bi)
    table[Bi].add(Ai)
answer = 0
for i, h in enumerate(H):
    highest = True
    for path in table[i]:
        if h <= H[path]:
            highest = False
    if highest:
        answer += 1
print(answer)
