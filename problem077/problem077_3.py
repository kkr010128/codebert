a, b, c, d = map(int, input().split())

ans = -float("INF")  # 答えがマイナスになることがあるので、負の無限大を初期値にしておきます

for x in (a, b):
    for y in (c, d):
        ans = max(ans, x * y)

print(ans)