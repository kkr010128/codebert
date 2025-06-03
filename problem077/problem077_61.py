# -*- coding: utf-8 -*-

def get_input() -> tuple:
    """
    標準入力を取得する.

    Returns:\n
        tuple: 標準入力
    """
    a, b, c, d = list(map(int, input().split()))

    return a, b, c, d


def main(a: int, b: int, c: int, d: int) -> None:
    """
    メイン処理.

    Args:\n
        a (int): 整数(-10**9 <= a <= b <= 10**9)
        b (int): 整数(-10**9 <= a <= b <= 10**9)
        c (int): 整数(-10**9 <= c <= d <= 10**9)
        d (int): 整数(-10**9 <= c <= d <= 10**9)
    """
    # 求解処理
    ans = max([a * c, a * d, b * c, b * d])

    # 結果出力
    print(ans)


if __name__ == "__main__":
    # 標準入力を取得
    a, b, c, d = get_input()

    # メイン処理
    main(a, b, c, d)
