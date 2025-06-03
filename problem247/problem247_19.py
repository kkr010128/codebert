import sys
import fractions

readline = sys.stdin.buffer.readline


def main():
    gcd = fractions.gcd

    def lcm(a, b):
        return a * b // gcd(a, b)

    N, M = map(int, readline().split())
    A = list(set(map(int, readline().split())))

    B = A[::]
    while not any(b % 2 for b in B):
        B = [b // 2 for b in B]

    if not all(b % 2 for b in B):
        print(0)
        return

    semi_lcm = 1
    for a in A:
        semi_lcm = lcm(semi_lcm, a // 2)
        if semi_lcm > M:
            print(0)
            return

    print((M // semi_lcm + 1) // 2)
    return


if __name__ == '__main__':
    main()
