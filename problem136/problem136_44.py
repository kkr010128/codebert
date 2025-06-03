import sys
from io import StringIO
import unittest
import os

# 再帰処理上限(dfs作成時に設定するのが面倒なので限度近い値を組み込む)
sys.setrecursionlimit(999999999)


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if not arr:
        arr.append([n, 1])

    return arr


# 実装を行う関数
def resolve(test_def_name=""):
    n = int(input())

    target_s = factorization(n)

    # 素因数1だけ処理対象外。
    if sum([i[1] for i in target_s]) == 1:
        if target_s[0][0] == 1:
            print(0)
        else:
            print(1)
        return

    # 少ない物から使っていく。
    cnt = 0
    for i in range(1, 1000):

        if not any([True if j[1] >= i else False for j in target_s]):
            break

        for target in target_s:
            if target[1] < i:
                continue
            target[1] -= i
            cnt += 1

    print(cnt)


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
        test_input = """24"""
        output = """3"""
        self.assertIO(test_input, output)

    def test_input_2(self):
        test_input = """1"""
        output = """0"""
        self.assertIO(test_input, output)

    def test_input_3(self):
        test_input = """64"""
        output = """3"""
        self.assertIO(test_input, output)

    def test_input_4(self):
        test_input = """1000000007"""
        output = """1"""
        self.assertIO(test_input, output)

    def test_input_5(self):
        test_input = """997764507000"""
        output = """7"""
        self.assertIO(test_input, output)

    def test_1original_1(self):
        test_input = """108"""
        output = """3"""
        self.assertIO(test_input, output)


# 実装orテストの呼び出し
if __name__ == "__main__":
    if os.environ.get("USERNAME") is None:
        # AtCoder提出時の場合
        resolve()

    else:
        # 自PCの場合
        unittest.main()
