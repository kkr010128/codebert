def prime_factorize(n):
    a = [1]
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

A,B = map(int,input().split())
div_A = set(prime_factorize(A))
div_B = set(prime_factorize(B))
A_and_B = div_A & div_B
print(len(A_and_B))