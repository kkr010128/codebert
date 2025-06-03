# -*- coding: utf-8 -*-
# モジュールのインポート
import math


def get_input() -> int:
    """
    標準入力を取得する.

    Returns:\n
        int: 標準入力
    """
    S = int(input())

    return S


def combinations_count(n: int, r: int) -> int:
    """
    組み合わせの総数を取得する.

    Args:\n
        n (int): 整数
        r (int): 整数(r <= n)

    Returns:\n
        int: 組み合わせの総数
    """
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


def main(S: int) -> None:
    """
    メイン処理.

    Args:\n
        S (int): 整数(1 <= S <= 2000)
    """
    # 求解処理
    a = S // 3
    b = S % 3
    ans = 0
    while a > 0:
        ans += combinations_count(b + a - 1, b)
        a -= 1
        b += 3
    ans %= 10**9 + 7

    # 結果出力
    print(ans)


if __name__ == "__main__":
    # 標準入力を取得
    S = get_input()

    # メイン処理
    main(S)
