from collections import Counter
N, X, Y = map(int, input().split())

ans = []
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        min_dis = min(abs(j - i),
                      abs(X - i) + 1 + abs(j - Y),
                      abs(Y - i) + 1 + abs(j - X))
        ans.append(min_dis)

c = Counter(ans)
for i in range(1, N):
    print(c[i])
