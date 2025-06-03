import sys
from io import StringIO
import unittest
import os

# 再帰処理上限(dfs作成時に設定するのが面倒なので限度近い値を組み込む)
sys.setrecursionlimit(999999999)


def prepare_simple(n, mod=pow(10, 9) + 7):
    # n! の計算
    f = 1
    for m in range(1, n + 1):
        f *= m
        f %= mod
    fn = f

    # n!^-1 の計算
    inv = pow(f, mod - 2, mod)
    # n!^-1 - 1!^-1 の計算
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= mod
        invs[m - 1] = inv
    return fn, invs


def prepare(n, mod=pow(10, 9) + 7):
    # 1! - n! の計算
    f = 1
    factorials = [1]  # 0!の分
    for m in range(1, n + 1):
        f *= m
        f %= mod
        factorials.append(f)
    # n!^-1 の計算
    inv = pow(f, mod - 2, mod)
    # n!^-1 - 1!^-1 の計算
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= mod
        invs[m - 1] = inv

    return factorials, invs


# 実装を行う関数
def resolve(test_def_name=""):
    x, y = map(int, input().split())

    all_move_count = (x + y) // 3

    x_move_count = all_move_count
    y_move_count = 0

    x_now = all_move_count * 2
    y_now = all_move_count

    canMake= False
    for i in range(all_move_count+1):
        if x_now == x and y_now == y:
            canMake = True
            break

        x_move_count -= 1
        y_move_count += 1
        x_now -= 1
        y_now += 1

    if not canMake:
        print(0)
        return

    fns, invs = prepare(all_move_count)
    ans = (fns[all_move_count] * invs[x_move_count] * invs[all_move_count - x_move_count]) % (pow(10, 9) + 7)

    print(ans)
    # fn, invs = prepareSimple(10)
    # ans = (fn * invs[3] * invs[10 - 3]) % (pow(10, 9) + 7)
    # print(ans)


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
        test_input = """3 3"""
        output = """2"""
        self.assertIO(test_input, output)

    def test_input_2(self):
        test_input = """2 2"""
        output = """0"""
        self.assertIO(test_input, output)

    def test_input_3(self):
        test_input = """999999 999999"""
        output = """151840682"""
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
