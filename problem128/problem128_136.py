def abc170_c_2():
    """
    もっとシンプルに考えると
    Xから-1、+1と順番に探索して、見つかったものをリターンすればOKなはず。
    ±0～99までを調べる？
    """
    def solve():
        x, n = map(int, input().split(' '))
        if n == 0:
            return x

        p = list(map(int, input().split(' ')))

        for i in range(100):
            for s in [-1, +1]:
                a = x + i * s
                if a not in p:
                    return a
    print(solve())

if __name__ == '__main__':
    abc170_c_2()