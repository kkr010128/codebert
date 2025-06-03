import sys
from io import StringIO
import unittest
import os

# 再帰処理上限(dfs作成時に設定するのが面倒なので限度近い値を組み込む)
sys.setrecursionlimit(999999999)


# 実装を行う関数
def resolve(test_def_name=""):
    n, k = map(int, input().split())

    ans = 0

    min_num = 0
    desk_list = list(reversed(range(n + 1)))

    max_num = 0
    ack_list = list(range(n + 1))

    for i in range(1, n + 1):
        min_num = (min_num + desk_list.pop()) % (pow(10, 9) + 7)
        max_num = (max_num + ack_list.pop()) % (pow(10, 9) + 7)
        if k <= i:
            ans = (ans + max_num - min_num + 1) % (pow(10, 9) + 7)

    print(ans+1)


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
        test_input = """3 2"""
        output = """10"""
        self.assertIO(test_input, output)

    def test_input_2(self):
        test_input = """200000 200001"""
        output = """1"""
        self.assertIO(test_input, output)

    def test_input_3(self):
        test_input = """141421 35623"""
        output = """220280457"""
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
