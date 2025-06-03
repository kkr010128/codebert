def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b


def pf(v):
    result = 1
    for i in range(2, v + 1):
        if v < i * i:
            if v > 1:
                result += 1
            break
        if v % i == 0:
            result += 1
        while v > 1 and v % i == 0:
            v //= i
    return result


a, b = list(map(int, input().split()))
print(pf(gcd(a, b)))
