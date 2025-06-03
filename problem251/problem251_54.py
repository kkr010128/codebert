N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()
points = {'r': P, 's': R, 'p': S}
is_changed = [False] * K + [False] * (N - K)
score = 0
for i in range(K):
    score += points[T[i]]

for i in range(K, N):
    if T[i] == T[i - K] and not is_changed[i - K]:
        is_changed[i] = True
    else:
        score += points[T[i]]

print(score)
