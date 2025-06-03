def input_li():
    return list(map(int, input().split()))


def input_int():
    return int(input())


def prime_factorization(n):
    table = []
    for x in range(2, int(n ** 0.5) + 1):
        while n % x == 0:
            table.append(x)
            n //= x
    if n > 1:
        table.append(n)
    return table


A, B = input_li()
A_SET = set(prime_factorization(A))
B_SET = set(prime_factorization(B))
print(len(A_SET & B_SET) + 1)
