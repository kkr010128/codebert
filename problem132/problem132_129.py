from itertools import accumulate
n,k = map(int, input().split())
As = list(map(int, input().split()))
for i in range(k):
    imos = [0] * (n+1)
    for i,a in enumerate(As):
        l = max(0, i-a)
        r = min(n, i+a+1)
        imos[l] += 1
        imos[r] -= 1
    acc = list(accumulate(imos))
    # 指数関数的に増える
    if acc[:-1] == As:
        print(*As)
        exit()
    As = acc[:-1]
print(*As)