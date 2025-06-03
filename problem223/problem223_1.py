import sys
from builtins import enumerate
from io import StringIO
import unittest
import os

# 再帰処理上限(dfs作成時に設定するのが面倒なので限度近い値を組み込む)
sys.setrecursionlimit(999999999)


# 実装を行う関数
def resolve(test_def_name=""):
    # 数値取得サンプル
    #   1行1項目 n = int(input())
    #   1行2項目 x, y = map(int, input().split())
    #   1行N項目 x = list(map(int, input().split()))
    #   N行1項目 x = [int(input()) for i in range(n)]
    #   N行N項目 x = [list(map(int, input().split())) for i in range(n)]

    # 文字取得サンプル
    #   1行1項目 x = input()
    #   1行1項目(1文字ずつリストに入れる場合) x = list(input())
    n, k = map(int, input().split())
    p_s = [0] + list(map(int, input().split()))

    avr_s = [0]
    cumsum = 0
    for i in range(1, 1001):
        cumsum += i
        avr_s.append(cumsum / i)

    ans = 0
    val = 0
    for i in range(1, len(p_s)):
        val += avr_s[p_s[i]]
        if i < k:
            continue
        elif i == k:
            ans = val
        else:
            val -= avr_s[p_s[i - k]]
            ans = max(ans, val)

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
        test_input = """5 3
1 2 2 4 5"""
        output = """7.000000000000"""
        self.assertIO(test_input, output)

    def test_input_2(self):
        test_input = """4 1
6 6 6 6"""
        output = """3.500000000000"""
        self.assertIO(test_input, output)

    def test_input_3(self):
        test_input = """10 4
17 13 13 12 15 20 10 13 17 11"""
        output = """32.000000000000"""
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
