import sys
def input():
    return sys.stdin.readline()[:-1]


def main():
    N, K = map(int,input().split())
    mod = 10 ** 9 + 7
    ans = 0
    for i in range(K, N + 1 + 1):
        mi = int((i - 1) * i / 2)  #ma、miは i * (10 **100)を無視した上限下限
        ma = i * N - mi
        ans += ma - mi + 1
    print(ans % mod)


if __name__ == "__main__":
    main()