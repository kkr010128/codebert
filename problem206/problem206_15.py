# -*- coding: utf-8 -*-
# モジュールのインポート
import math


def get_input() -> int:
    """
    標準入力の取得

    Returns:\n
        int: 標準入力
    """
    N = int(input())

    return N


def main(N: int) -> None:
    """
    求解処理

    Args:
        N (int): ページ数
    """
    result = math.ceil(N/2)

    # 結果出力
    print(result)


if __name__ == "__main__":
    N = get_input()
    main(N)
