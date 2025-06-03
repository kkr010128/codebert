# coding: UTF-8

CONTEST_NUM = 26

class Optimizer:

    def __init__(self, days, s, c):
        self._days = days
        self._s = s
        self._c = c

    def optimize(self):
        # 貪欲法による手法
        t = []
        for d in range(self._days):
            max_d_value = 0
            max_contest = 0
            for i in range(CONTEST_NUM):
                d_value = self._s[d][i] + self._c[i] * (d + 1)
                if d_value > max_d_value:
                    max_d_value = d_value
                    max_contest = i
            t.append(max_contest + 1)
        return t


def main():
    ## 引数読み込み
    days = int(input()) # D
    c = tuple(map(int, input().split())) # c[i]
    s = [] # s[d][i]
    for i in range(days):
        s.append(tuple(map(int, input().split())))

    ## 試しに指標計算
    t = Optimizer(days, s, c).optimize()

    ## print out
    for v in t:
        print(v)

if __name__ == "__main__":
    main()
