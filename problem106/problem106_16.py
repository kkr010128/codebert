# -*- coding: utf-8 -*-
# モジュールのインポート
import math
import itertools


def get_input() -> int:
    """
    標準入力を取得する.

    Returns:\n
        int: 標準入力
    """
    N = int(input())

    return N

# メイン処理


def g(x: int, y: int, z: int) -> int:
    """
    関数.

    Args:\n
        x (int): 整数（1 <= x）
        y (int): 整数（1 <= y）
        z (int): 整数（1 <= z）

    Returns:\n
        int: 関数値
    """
    return x**2 + y**2 + z**2 + x*y + y*z + z*x


def main(N: int) -> None:
    """
    メイン処理.

    Args:\n
        N (int): 整数
    """
    # 求解処理
    l = [0 for n in range(N)]
    ub = int(math.sqrt(N))
    for x, y, z in itertools.product(range(1, ub + 1), repeat=3):
        v = g(x, y, z)
        if v <= N:
            l[v - 1] += 1

    # 結果出力
    for ans in l:
        print(ans)


if __name__ == "__main__":
    # 標準入力を取得
    N = get_input()

    # メイン処理
    main(N)
