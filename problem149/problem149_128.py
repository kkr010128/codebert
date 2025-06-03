n, m, x = map(int, input().split())
books = [list(map(int, input().split())) for _ in range(n)]
INF = 10 ** 9 + 7

ans = INF
for bits in range(2 ** n):
    cost = 0
    score = [0] * m
    for i, book in enumerate(books):
        if bits >> i & 1:
            cost += book[0]
            score = [s + b for s, b in zip(score, book[1:])]
    if all(s >= x for s in score):
        ans = min(ans, cost)

if ans == INF:
    print(-1)
else:
    print(ans)