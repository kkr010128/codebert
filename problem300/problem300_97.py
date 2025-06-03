def prime_factorization(n):
    table = []
    for x in range(2, int(n ** 0.5) + 1):
        while n % x == 0:
            table.append(x)
            n //= x
    if n > 1:
        table.append(n)
    return table


A, B = map(int, input().split())
ad = set(prime_factorization(A))
bd = set(prime_factorization(B))

cnt = 0
for a in ad:
    if a in bd:
        cnt += 1
print(cnt+1)
