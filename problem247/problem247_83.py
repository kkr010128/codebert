import sys
import math

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def LCM(a, b):
    return a * b // math.gcd(a, b)


def main():
    N, M = in_nn()
    a = in_nl()

    lcm = 1
    for i in range(N):
        lcm = LCM(lcm, a[i])
        if lcm > M * 2:
            print(0)
            exit()

    for i in range(N):
        if lcm // a[i] % 2 == 0:
            print(0)
            exit()

    lcm = lcm // 2
    q = M // lcm
    if q % 2 == 0:
        ans = q // 2
    else:
        ans = q // 2 + 1

    print(ans)


if __name__ == '__main__':
    main()
