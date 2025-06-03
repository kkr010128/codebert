import sys
from io import StringIO
import unittest
import os
from collections import deque

# 再帰処理上限(dfs作成時に設定するのが面倒なので限度近い値を組み込む)
sys.setrecursionlimit(999999999)


# 実装を行う関数
def resolve(test_def_name=""):
    # 数値取得サンプル
    #   1行1項目 n = int(input())
    #   1行2項目 h, w = map(int, input().split())
    #   1行N項目 x = list(map(int, input().split()))
    #   N行1項目 x = [int(input()) for i in range(n)]
    #   N行N項目 x = [list(map(int, input().split())) for i in range(n)]

    # 文字取得サンプル
    #   1行1項目 x = input()
    #   1行1項目(1文字ずつリストに入れる場合) x = list(input())
    h, w = map(int, input().split())
    maze = [list(input()) for i in range(h)]

    start_list = []
    for i_len, i in enumerate(range(h)):
        for j_len, j in enumerate(range(w)):
            route = 4
            # 自分が壁なら対象外
            if maze[i][j] == "#":
                continue

            # 上下端なら-1
            route -= 1 if i_len == 0 else 0
            route -= 1 if i_len + 1 == h else 0
            # 上下が壁なら-1
            route -= 1 if not i_len == 0 and maze[i - 1][j] == "#" else 0
            route -= 1 if not i_len + 1 == h and maze[i + 1][j] == "#" else 0
            # 左右端なら-1
            route -= 1 if j_len == 0 else 0
            route -= 1 if j_len + 1 == w else 0
            # 左右が壁なら-1
            route -= 1 if not j_len == 0 and maze[i][j - 1] == "#" else 0
            route -= 1 if not j_len + 1 == w and maze[i][j + 1] == "#" else 0
            if route <= 2:
                start_list.append((i, j))

    ans = 0
    que = deque()
    for start in start_list:
        que.appendleft(start)
        ed_list = [[-1 for i in range(w)] for j in range(h)]
        ed_list[start[0]][start[1]] = 0

        # BFS開始
        while len(que) is not 0:
            now = que.pop()

            # 各方向に移動
            for i, j in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
                # 処理対象の座標
                target = [now[0] + i, now[1] + j]

                # 処理対象のチェック
                # 外なら何もしない
                if not 0 <= target[0] < h or not 0 <= target[1] < w:
                    continue

                # 距離が設定されているなら何もしない
                if ed_list[target[0]][target[1]] != -1:
                    continue

                # 壁なら何もしない
                if maze[target[0]][target[1]] == "#":
                    continue

                # 処理対象に対する処理
                # キューに追加(先頭に追加するのでappendleft())
                que.appendleft(target)
                # 距離を設定(現在の距離+1)
                ed_list[target[0]][target[1]] = ed_list[now[0]][now[1]] + 1
                ans = max(ans, ed_list[target[0]][target[1]])

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
        test_input = """3 3
...
...
..."""
        output = """4"""
        self.assertIO(test_input, output)

    def test_input_2(self):
        test_input = """3 5
...#.
.#.#.
.#..."""
        output = """10"""
        self.assertIO(test_input, output)

    # 自作テストパターンのひな形(利用時は「tes_t」のアンダーバーを削除すること
    def test_1original_1(self):
        test_input = """1 2
.."""
        output = """1"""
        self.assertIO(test_input, output)


# 実装orテストの呼び出し
if __name__ == "__main__":
    if os.environ.get("USERNAME") is None:
        # AtCoder提出時の場合
        resolve()

    else:
        # 自PCの場合
        unittest.main()
