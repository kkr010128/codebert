import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N = int(readline())
    A = list(map(int, readline().split()))
    R = 0
    G = 0
    B = 0
    ans = 1
    for a in A:
        if a == R == G == B:
            ans *= 3
            ans %= MOD
            R += 1
        else:
            if a == R == G:
                ans *= 2
                ans %= MOD
                R += 1
            elif a == G == B:
                ans *= 2
                ans %= MOD
                G += 1
            elif a == B == R:
                ans *= 2
                ans %= MOD
                B += 1
            else:
                if a == R:
                    R += 1
                elif a == G:
                    G += 1
                elif a == B:
                    B += 1
                else:
                    print(0)
                    sys.exit()
    print(ans % MOD)


if __name__ == '__main__':
    main()
