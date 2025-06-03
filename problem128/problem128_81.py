X, N = map(int, input().split())
p = list(map(int, input().split()))

for i in range(X + 1):
    for j in [-1, +1]:
        ans = X + i * j

        if p.count(ans) == 0:
            print(ans)
            break
    else:
        continue
    break
