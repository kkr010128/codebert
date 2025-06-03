def gcd(m, n):
    x = max(m, n)
    y = min(m, n)
    if x % y == 0:
        return y
    else:
        while x % y != 0:
            z = x % y
            x = y
            y = z
        return z


def lcm(m, n):
    return (m * n) // gcd(m, n)


# input
A, B = map(int, input().split())

# lcm
snack = lcm(A, B) 

print(snack)
