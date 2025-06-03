import sys


def popcount(x: int):
    return bin(x).count("1")


def main():
    N = int(sys.stdin.readline().rstrip())
    X = sys.stdin.readline().rstrip()

    Xdec = int(X, 2)

    # 1回目の演算用
    md = popcount(Xdec)
    md_p, md_m = md + 1, md - 1

    tmp_p = Xdec % md_p
    if md_m > 0:
        tmp_m = Xdec % md_m

    for i in range(0, N, 1):
        if X[i] == "1":  # 1->0
            if md_m == 0:
                print(0)
                continue
            x_m = pow(2, (N - 1 - i), md_m)
            tmp = (tmp_m - x_m) % md_m

        if X[i] == "0":  # 0->1
            x_p = pow(2, (N - 1 - i), md_p)
            tmp = (tmp_p + x_p) % md_p

        cnt = 1
        while tmp:

            tmp = tmp % popcount(tmp)
            cnt += 1

        print(cnt)


main()
