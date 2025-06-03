import sys
from io import StringIO
import unittest
import os


# 実装を行う関数
def resolve():
    # 数値取得サンプル
    #   1行N項目 x, y = map(int, input().split())
    #   N行N項目 x = [list(map(int, input().split())) for i in range(n)]
    n = int(input())
    bricks = list(map(int, input().split()))

    # 1が無ければ-1
    if 1 not in bricks:
        print(-1)
        return

    num = 1
    ban = 0
    for brick in bricks:
        if brick == num:
            num += 1
            continue
        ban += 1

        # dev
        1 == 1

    print(ban)





    # 文字取得サンプル
    #   1行1項目 x = input()
    pass


# テストクラス
class TestClass(unittest.TestCase):
    def assertIO(self, assert_input, output):
        stdout, sat_in = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(assert_input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, sat_in
        self.assertEqual(out, output)

    def test_input_1(self):
        test_input = """3
2 1 2"""
        output = """1"""
        self.assertIO(test_input, output)

    def test_input_2(self):
        test_input = """3
2 2 2"""
        output = """-1"""
        self.assertIO(test_input, output)

    def test_input_3(self):
        test_input = """10
3 1 4 1 5 9 2 6 5 3"""
        output = """7"""
        self.assertIO(test_input, output)

    def test_input_4(self):
        test_input = """1
1"""
        output = """0"""
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
