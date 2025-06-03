import sys
from io import StringIO
import unittest
import os
from operator import ixor

# 再帰処理上限(dfs作成時に設定するのが面倒なので限度近い値を組み込む)
sys.setrecursionlimit(999999999)


# 実装を行う関数
def resolve(test_def_name=""):
    # 数値取得サンプル
    #   1行1項目 n = int(input())
    #   1行2項目 x, y = map(int, input().split())
    #   1行N項目 x = [list(map(int, input().split()))]
    #   N行1項目 x = [int(input()) for i in range(n)]
    #   N行N項目 x = [list(map(int, input().split())) for i in range(n)]

    # 文字取得サンプル
    #   1行1項目 x = input()
    #   1行1項目(1文字ずつリストに入れる場合) x = list(input())
    n = int(input())
    a_s = list(map(int, input().split()))

    one_counts = [0 for i in range(61)]
    zero_counts = [0 for i in range(61)]

    # 以下、XORで便利と思われる処理。
    # -------------------------------------------
    # ループ回数の取得(最大の数値の桁数分、ループ処理を行うようにする)
    max_num = max(a_s)
    max_loop = 0
    for i in range(0, 61):
        if max_num < 1 << i:
            break
        max_loop += 1

    # ループ処理にて、各桁の0と1の個数を数え上げる。
    # 例：入力[1(01),2(10),3(11)] -> one_count=[2,2,0・・]とzero_counts[1,1,0・・]を得る。
    for a in a_s:
        for i in range(0, max_loop):
            if a & 1 << i:
                one_counts[i] += 1
            else:
                zero_counts[i] += 1
    # -------------------------------------------
    # 以上、XORで便利と思われる処理。

    # 結果を計算する処理
    ans = 0
    for i in range(0, max_loop):
        # 各桁の「0の個数」*「1の個数」*2^(0～桁数-1乗まで) を加算していく
        ans += (one_counts[i] * zero_counts[i] * pow(2, i)) % (pow(10, 9) + 7)
        ans = ans % (pow(10, 9) + 7)

    # 結果を出力
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
        test_input = """3
1 2 3"""
        output = """6"""
        self.assertIO(test_input, output)

    def test_input_2(self):
        test_input = """10
3 1 4 1 5 9 2 6 5 3"""
        output = """237"""
        self.assertIO(test_input, output)

    def test_input_3(self):
        test_input = """10
3 14 159 2653 58979 323846 2643383 27950288 419716939 9375105820"""
        output = """103715602"""
        self.assertIO(test_input, output)

    # 自作テストパターンのひな形(利用時は「tes_t」のアンダーバーを削除すること
    def tes_t_1original_1(self):
        test_input = """データ"""
        output = """データ"""
        self.assertIO(test_input, output)


# 実装orテストの呼び出し
if __name__ == "__main__":
    if os.environ.get("USERNAME") is None:
        # AtCoder提出時の場合
        resolve()

    else:
        # 自PCの場合
        unittest.main()
