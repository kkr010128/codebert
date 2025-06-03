X = list(map(int, input().split()))

ans = None
for i, xi in enumerate(X):
    if xi == 0:
        ans = i + 1

print(ans)