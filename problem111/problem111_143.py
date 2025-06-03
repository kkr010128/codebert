import sys
from io import StringIO
import unittest
import os
import heapq

# 再帰処理上限(dfs作成時に設定するのが面倒なので限度近い値を組み込む)
sys.setrecursionlimit(999999999)


# 検索用タグ、優先度付きキュー、値の大きい物から取得

# 実装を行う関数
def resolve(test_def_name=""):
    n = int(input())
    a_s = list(map(int, input().split()))

    a_s.sort(reverse=True)

    # 優先度付きキューの作成
    que = []
    heapq.heapify(que)

    ans = 0
    # 大きい値から順番に処理していく
    for cnt, a in enumerate(a_s):
        # 大きい値から順番に処理していくため、値を反転(優先度付きキュー利用時の注意)
        a = -a
        if cnt == 0:
            # ループ一回目の時だけ、こっちを通過。
            heapq.heappush(que, a)
            continue

        # キューから値の取り出し
        target = heapq.heappop(que)
        ans += -target
        # 現在の値を追加できるパターンが2つできるので、それをキューに追加
        heapq.heappush(que, a)
        heapq.heappush(que, a)

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
        test_input = """4
2 2 1 3"""
        output = """7"""
        self.assertIO(test_input, output)

    def test_input_2(self):
        test_input = """7
1 1 1 1 1 1 1"""
        output = """6"""
        self.assertIO(test_input, output)

    # 自作テストパターンのひな形(利用時は「tes_t」のアンダーバーを削除すること
    def test_1original_1(self):
        test_input = """4
2 2 3 3"""
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
