import sys
from io import StringIO
import unittest
import os
import math

# 再帰処理上限(dfs作成時に設定するのが面倒なので限度近い値を組み込む)
sys.setrecursionlimit(999999999)


# 0 = 1桁目
def digit_val(number, n) -> int:
    return number // 10 ** n % 10


def max_digit_val(number) -> int:
    return number // 10 ** int(math.log10(number)) % 10


def min_digit_val(number) -> int:
    return number // 10 ** 0 % 10


def int_len(number) -> int:
    return int(math.log10(number) + 1)


# 実装を行う関数
def resolve(test_def_name=""):
    n = int(input())

    # 対象となる数字の一覧を作成(1～20万の数字かつ、0を含まない数字)
    target_list = []
    ignore_cnt = 0
    for i in range(1, n + 1):
        ignore_cnt += 1
        if ignore_cnt == 10:
            ignore_cnt = 0
            continue
        target_list.append(i)

    # 先頭X で末尾Y という数字がいくつ存在するか・・というカウンタを作成。
    cnt_dict = {}
    for i in target_list:
        if int_len(i) == 1:
            # 1桁目の場合は最初桁と最後桁が同じ
            cnt_dict[i * 10 + i] = cnt_dict.get(i * 10 + i, 0) + 1
        else:
            val = max_digit_val(i) * 10 + min_digit_val(i)
            cnt_dict[val] = cnt_dict.get(val, 0) + 1

    # 使用できるパターンを足し込みしていく。
    ans = 0
    for i in target_list:
        if int_len(i) == 1:
            ans += cnt_dict.get(i * 10 + i, 0)
        else:
            val = min_digit_val(i) * 10 + max_digit_val(i)
            ans += cnt_dict.get(val, 0)

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
        test_input = """25"""
        output = """17"""
        self.assertIO(test_input, output)

    def test_input_2(self):
        test_input = """1"""
        output = """1"""
        self.assertIO(test_input, output)

    def test_input_3(self):
        test_input = """100"""
        output = """108"""
        self.assertIO(test_input, output)

    def test_input_4(self):
        test_input = """2020"""
        output = """40812"""
        self.assertIO(test_input, output)

    def test_input_5(self):
        test_input = """200000"""
        output = """400000008"""
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
