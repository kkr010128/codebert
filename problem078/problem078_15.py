import sys
input = sys.stdin.readline


def main():
    mod = 10**9 + 7
    n = int(input())
    all = pow(10, n, mod)
    non_0 = non_9 = pow(9, n, mod)
    non_0_and_9 = pow(8, n, mod)
    ans = all - non_0 - non_9 + non_0_and_9
    print(ans % mod)


if __name__ == "__main__":
    main()
