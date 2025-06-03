# C - Subarray Sum
def main():
    N, K, S = map(int, input().split())
    res = [str(S)] * K + ["1" if S == 10 ** 9 else str(S + 1)] * (N - K)
    print(" ".join(res))


if __name__ == "__main__":
    main()
