def prime_factors(n):       # 戻り値はiterable type
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            yield i             # whileループを進めるごとにイテレータに値を貯め続ける
    if n > 1:
        yield n

A, B = map(int, input().split())

data = set(prime_factors(A)) & set(prime_factors(B))
print(len(data) + 1)
