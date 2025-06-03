import math


def main():

    mod = 1000000007
    N = int(input())

    A = [0]
    B = [0]

    for n in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    calc = dict()
    non_count = 0

    for i in range(1, N + 1):

        if A[i] == 0 and B[i] == 0:
            non_count += 1
        elif A[i] == 0:
            k = (0, 1)
            if calc.get(k):
                calc[k][0] += 1
            else:
                calc[k] = [1, 0]
        elif B[i] == 0:
            k = (0, 1)
            if calc.get(k):
                calc[k][1] += 1
            else:
                calc[k] = [0, 1]
        else:
            r = math.gcd(A[i], B[i])
            m = 1
            if A[i] * B[i] < 0:
                m = -1
            k1 = (m * abs(A[i] // r), abs(B[i] // r))
            k2 = (-m * abs(B[i] // r), abs(A[i] // r))
            if calc.get(k1):
                calc[k1][0] += 1
            elif not calc.get(k2):
                calc[k1] = [1, 0]
            else:
                calc[k2][1] += 1

    N = N - non_count

    count = 0
    for k, v in calc.items():
        if not v[0] * v[1] == 0:
            count += v[0] + v[1]

    ans = pow(2, N - count, mod)
    for k, v in calc.items():
        if not v[0] * v[1] == 0:
            comb = (pow(2, v[0]) + pow(2, v[1]) - 1)
            ans = (ans * comb) % mod

    print((ans - 1 + non_count) % mod)


if __name__ == '__main__':
    main()
