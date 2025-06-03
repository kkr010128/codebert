def coin_change(coins, payment):
    T = [0] + [50001] * payment
    for c in coins:
        for i, t in enumerate(zip(T[c:], T), start=c):
            a, b = t
            T[i] = min(a, b + 1)
    return T[payment]

n, m = map(int, input().split())

c = list(map(int, input().split()))

ans = coin_change(c, n)

print(ans)