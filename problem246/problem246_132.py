# -*- coding: utf-8 -*-
# モジュールのインポート
import itertools


def get_input() -> tuple:
    """
    標準入力を取得する.

    Returns:\n
        tuple: 標準入力
    """
    # 標準入力を取得
    N = int(input())
    P = tuple(map(int, input().split()))
    Q = tuple(map(int, input().split()))

    return N, P, Q


def main(N: int, P: tuple, Q: tuple) -> None:
    """
    メイン処理.

    Args:\n
        N (int): 数列の大きさ
        P (tuple): 順列
        Q (tuple): 順列
    """
    # 求解処理
    p = 0
    q = 0
    order = 1
    for t in itertools.permutations(range(1, N + 1), N):
        if t == P:
            p = order
        if t == Q:
            q = order
        order += 1

    ans = abs(p - q)

    # 結果出力
    print(ans)


if __name__ == "__main__":
    # 標準入力を取得
    N, P, Q = get_input()

    # メイン処理
    main(N, P, Q)
