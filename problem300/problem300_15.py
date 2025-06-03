def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3

    # for f in range(3,int(n**0.5)+1,2):
    #     if n%f == 0:
    #         a.append(f)
    #         n //= f
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

a, b = list(map(int,input().split()))
A, B = set(prime_factorize(a)), set(prime_factorize(b))
C = A&B
# print(A,B,C)

print(len(C)+1)