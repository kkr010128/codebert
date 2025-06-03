def main():
    """
    a % d + c % d = (a + c) % dだ
    整数の余りを取るのと，整数の各桁の余りを取るのが同じを使うこともあった　→　Digits Parade
    """
    N = int(input())
    X = input()
    t = X.count("1")
    v1, v2 = int(X, 2) % (t+1), int(X, 2) % (t-1) if t != 1 else 0
    for i in range(N):
        ans = 1
        x = 0
        if X[i] == "0":
            # 反転してt+1
            x = v1 + pow(2, N-i-1, t+1)
            x %= t+1
        elif t != 1 and X[i] == "1":
            # 反転してt-1
            x = v2 - pow(2, N-i-1, t-1)
            x %= t-1
        else:
            # t == 1 かつ その"1"を反転するとき
            # 当然X_iは0になる，答えも0
            ans = 0
        while x > 0:
            x %= "{:0b}".format(x).count("1")
            ans += 1
        print(ans)


if __name__ == '__main__':
    main()
