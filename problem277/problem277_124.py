class Acc2D:
    def __init__(self, a):
        h, w = len(a), len(a[0])
        self.acc2D = self._build(h, w, a)

    def _build(self, h, w, a):
        ret = [[0] * (w + 1) for _ in range(h + 1)]
        for r in range(h):
            for c in range(w):
                ret[r + 1][c + 1] = ret[r][c + 1] + ret[r + 1][c] - ret[r][c] + (1 if a[r][c] == '#' else 0)
                # 末項は必要に応じて改変すること
        return ret

    def get(self, r1, r2, c1, c2):
        # [r1,r2), [c1,c2) : 0-indexed
        acc2D = self.acc2D
        return acc2D[r2][c2] - acc2D[r1][c2] - acc2D[r2][c1] + acc2D[r1][c1]


def main():
    import sys

    sys.setrecursionlimit(10 ** 7)

    def fill_cake(r1, r2, c1, c2) -> None:
        """ケーキに番号を振る"""
        nonlocal piece_number
        for r in range(r1, r2):
            for c in range(c1, c2):
                ret[r][c] = piece_number
        piece_number += 1

    def cut_cake(r1, r2, c1, c2, rest) -> None:
        """[r1,r2),[c1,c2)の範囲にrest個ケーキがある状態からのカット"""
        if rest == 1:
            fill_cake(r1=r1, r2=r2, c1=c1, c2=c2)
            return  # これ以上カットする必要がないので、番号を振る

        for r in range(r1 + 1, r2):
            piece_count = acc2D.get(r1=r1, r2=r, c1=c1, c2=c2)
            if 0 < piece_count < rest:  # restが減ることを保証する
                cut_cake(r1=r1, r2=r, c1=c1, c2=c2, rest=piece_count)
                cut_cake(r1=r, r2=r2, c1=c1, c2=c2, rest=rest - piece_count)
                return  # ケーキを一つ以上含むように水平カットする

        for c in range(c1 + 1, c2):
            piece_count = acc2D.get(r1=r1, r2=r2, c1=c1, c2=c)
            if 0 < piece_count < rest:  # restが減ることを保証する
                cut_cake(r1=r1, r2=r2, c1=c1, c2=c, rest=piece_count)
                cut_cake(r1=r1, r2=r2, c1=c, c2=c2, rest=rest - piece_count)
                return  # ケーキを一つ以上含むように垂直カットする

    h, w, k = map(int, input().split())
    s = [input() for _ in range(h)]

    acc2D = Acc2D(s)
    # usage: acc2D.get(r1,r2,c1,c2)
    # ケーキ個数の二次元累積和

    ret = [[-1] * w for _ in range(h)]
    piece_number = 1

    cut_cake(r1=0, r2=h, c1=0, c2=w, rest=k)

    for row in ret:
        print(*row)


if __name__ == '__main__':
    main()
