import sys
from io import StringIO
import unittest
import os

# 再帰処理上限(dfs作成時に設定するのが面倒なので限度近い値を組み込む)
sys.setrecursionlimit(999999999)


# 実装を行う関数
def resolve(test_def_name=""):
    h, w, k = map(int, input().split())
    s_s = [list(input()) for i in range(h)]

    # パターン数分の情報を作成(横に切る = 最大2^10個)
    # 全パターンの・・横に切る回数、と切る場所
    side = []
    for i in range(1 << h - 1):
        cut_cnt = 0
        point_s = []
        # パターンの桁数分ループ
        for j in range(h - 1):
            # フラグが立つ(bitが1)の場合の処理を以下に記載。
            if i & 1 << j:
                cut_cnt += 1
                point_s.append(j + 1)

        point_s.append(h)
        # 得た情報をリストに追加
        side.append([point_s, cut_cnt])

    ## 横切り必須にもかかわらず、横木入りしていないパターンを排除できていない・・と思われる。
    x_s_s = list(zip(*s_s))
    ans = 999999
    for side_cut_point_s, cut_cnt in side:
        # 横切りを実施した後の塊を取得
        cnt_s = [0 for i in range(cut_cnt + 1)]

        for x_s in x_s_s:
            start = 0
            for cnt, side_cut_point in enumerate(side_cut_point_s):
                cnt_s[cnt] += x_s[start: side_cut_point].count("1")
                start = side_cut_point
            # 切る必要がある場合は切る
            if max(cnt_s) > k:
                cut_cnt += 1
                start = 0
                for cnt, side_cut_point in enumerate(side_cut_point_s):
                    cnt_s[cnt] = x_s[start: side_cut_point].count("1")
                    start = side_cut_point
            if max(cnt_s) > k:
                cut_cnt += 99999
        ans = min(ans, cut_cnt)

    print(ans)


# テストクラス
class TestClass(unittest.TestCase):
    def assertIO(self, assert_input, output):
        stdout, sat_in = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(assert_input)
        resolve(sys._getframe().f_back.f_code.co_name)
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, sat_in
        self.assertEqual(out, output)

    def test_input_1(self):
        test_input = """3 5 4
11100
10001
00111"""
        output = """2"""
        self.assertIO(test_input, output)

    def test_input_2(self):
        test_input = """3 5 8
11100
10001
00111"""
        output = """0"""
        self.assertIO(test_input, output)

    def test_input_3(self):
        test_input = """4 10 4
1110010010
1000101110
0011101001
1101000111"""
        output = """3"""
        self.assertIO(test_input, output)

    # 自作テストパターンのひな形(利用時は「tes_t」のアンダーバーを削除すること
    def test_1original_1(self):
        test_input = """10 10 1
1000000000
1000000000
1000000000
1000000000
1000000000
1000000000
1000000000
1000000000
1000000000
1000000000"""
        output = """9"""
        self.assertIO(test_input, output)


# 実装orテストの呼び出し
if __name__ == "__main__":
    if os.environ.get("USERNAME") is None:
        # AtCoder提出時の場合
        resolve()

    else:
        # 自PCの場合
        unittest.main()
