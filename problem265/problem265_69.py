def main(N, rate=1.08):
    X = int(-(-N // 1.08))
    return X if int(X * rate) == N else -1


if __name__ == "__main__":
    N = int(input())
    ans = main(N)
    print(ans if ans > 0 else ':(')
