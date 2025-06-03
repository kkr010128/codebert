def Qc():
    x, n = map(int, input().split())
    if 0 < n:
        p = list(map(int, input().split()))
        for i in range(101):
            if x - i not in p:
                print(x - i)
                exit()
            if x + i not in p:
                res = x + 1
                print(x + i)
                exit()
    else:
        # 整数列がなにもない場合は自分自身が含まれていない最近値になる
        print(x)
        exit()


if __name__ == "__main__":
    Qc()
