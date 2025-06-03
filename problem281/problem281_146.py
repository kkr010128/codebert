def comb(n, m, p=10**9+7):
    if n < m:
        return 0
    if n < 0 or m < 0:
        return 0
    m = min(m, n-m)
    top = bot = 1
    for i in range(m):
        top = top*(n-i) % p
        bot = bot*(i+1) % p
    bot = pow(bot, p-2, p)
    return top*bot % p


x, y = map(int, input().split())

j = 2*x-y
if j % 3:
    print(0)
    exit()
j //= 3
i = x - 2*j
if i < 0 or j < 0:
    print(0)
    exit()

ans = comb(i+j, i)
print(ans)
