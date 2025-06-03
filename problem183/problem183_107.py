
N = int(input())


def calc_divisor(x):
    divisor = []
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            if i != 1:
                divisor.append(i)
            if i != x // i:
                divisor.append(x // i)
    return divisor


cand = len(calc_divisor(N - 1))
divisor_n = calc_divisor(N)
for v in divisor_n:
    x = N
    while x % v == 0:
        x //= v

    if x % v == 1:
        cand += 1

print(cand)
