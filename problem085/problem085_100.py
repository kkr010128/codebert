def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def main():
    N = int(input())
    A = [int(i) for i in input().split()]

    g = A[0]
    for i in range(1, N):
        g = gcd(g, A[i])

    if not g == 1:
        print('not coprime')
        return


    limit = int(10 ** 3)
    F = [0] * (10 ** 6 + 1)
    M = [0] * (10 ** 6 + 1)
    for i in range(2, limit + 1):
        if F[i] > 0:
            continue
        v = 2 * i
        while v <= 10 ** 6:
            if F[v] == 0:
                F[v] = i
            v += i

    pc = True
    for v in A:
        S = set()
        x = v
        while True:
            if F[x] > 0:
                S.add(F[x])
                x //= F[x]
            else:
                S.add(x)
                break

        for s in S:
            if s == 1:
                continue
            if M[s] == 1:
                pc = False
                break
            M[s] += 1

        if not pc:
            break

    if pc:
        print('pairwise coprime')
    else:
        print('setwise coprime')


if __name__ == '__main__':
    main()
