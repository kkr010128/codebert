import sys
from io import StringIO
import unittest
import os

# 再帰処理上限(dfs作成時に設定するのが面倒なので限度近い値を組み込む)
sys.setrecursionlimit(999999999)


class youk_prepare:
    def __init__(self, n, mod=pow(10, 9) + 7):
        f = 1
        factorials = [1]
        for m in range(1, n + 1):
            f *= m
            f %= mod
            factorials.append(f)
        inv = pow(f, mod - 2, mod)
        invs = [1] * (n + 1)
        invs[n] = inv
        for m in range(n, 1, -1):
            inv *= m
            inv %= mod
            invs[m - 1] = inv

        self.factorials = factorials
        self.invs = invs
        self.mod = mod

    def cmb(self, n, r):
        if len(self.factorials) - 1 < n:
            raise ValueError("コンストラクタで指定した要素数を超えているので無理。")
        return (self.factorials[n] * self.invs[r] * self.invs[n - r]) % self.mod

    def multi_cmb(self, n, r):
        if len(self.factorials) - 1 < n:
            raise ValueError("コンストラクタで指定した要素数を超えているので無理。")
        return (self.factorials[n] * self.invs[r] * self.invs[n - r]) * (
                self.factorials[n - 1] * self.invs[r] * self.invs[n - 1 - r]) % self.mod


# 実装を行う関数
def resolve(test_def_name=""):
    try:
        n, k = map(int, input().split())
        a_s = list(map(int, input().split()))

        a_s.sort()

        youk = youk_prepare(n)
        # 最小値の合計を計算
        sum_mini = 0
        for i in range(n - k + 1):
            target = a_s[i]
            val = target * youk.cmb(n - i - 1, k - 1)
            sum_mini += val

        # 最大値の合計を計算
        sum_max = 0
        for i in range(k - 1, n):
            target = a_s[i]
            val = target * youk.cmb(i, k - 1)
            sum_max += val

        ans = (sum_max - sum_mini) % (pow(10, 9) + 7)
        print(ans)


    except IndexError as err:
        print("インデックスエラー:", err.args[0])


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
        test_input = """4 2
1 1 3 4"""
        output = """11"""
        self.assertIO(test_input, output)

    def test_input_2(self):
        test_input = """6 3
10 10 10 -10 -10 -10"""
        output = """360"""
        self.assertIO(test_input, output)

    def test_input_3(self):
        test_input = """3 1
1 1 1"""
        output = """0"""
        self.assertIO(test_input, output)

    def test_input_4(self):
        test_input = """10 6
1000000000 1000000000 1000000000 1000000000 1000000000 0 0 0 0 0"""
        output = """999998537"""
        self.assertIO(test_input, output)

    # 自作テストパターン
    def test_original(self):
        test_input = """4 2
1 2 3 4"""
        output = """10"""
        self.assertIO(test_input, output)


# 実装orテストの呼び出し
if __name__ == "__main__":
    if os.environ.get("USERNAME") is None:
        # AtCoder提出時の場合
        resolve()

    else:
        # 自PCの場合
        unittest.main()
