import sys

input = sys.stdin.readline


def main():
    N = int(input())
    X = input()

    popcount_X = X.count("1")
    if popcount_X == 0:
        ans = [1] * N
    elif popcount_X == 1:
        ans = [1] * N
        ans[-1] = 2
        ans[X.index("1")] = 0
    else:
        X_mod_popcount_X_p = int(X, 2) % (popcount_X + 1)
        X_mod_popcount_X_m = int(X, 2) % (popcount_X - 1)
        ans = [0] * N
        for i in range(N):
            if X[i] == "0":
                Y = X_mod_popcount_X_p + pow(2, N - 1 - i, mod=popcount_X + 1)
                Y = Y % (popcount_X + 1)
            else:
                Y = X_mod_popcount_X_m - pow(2, N - 1 - i, mod=popcount_X - 1)
                Y = Y + (popcount_X - 1)
                Y = Y % (popcount_X - 1)
            count = 1
            while Y > 0:
                popcount = bin(Y).count("1")
                Y = Y % popcount
                count += 1
            ans[i] = count

    print("\n".join(map(str, ans)))


if __name__ == "__main__":
    main()
