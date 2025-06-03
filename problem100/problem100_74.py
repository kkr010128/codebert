# -*- coding: utf-8 -*-

def get_input() -> tuple:
    """
    標準入力を取得する.

    Returns:\n
        tuple: 標準入力
    """
    X = int(input())

    return X

def main(X: int) -> None:
    """
    メイン処理.

    Args:\n
        X (int): 最高レーティング（400 <= X <= 1999）
    """
    # 求解処理
    ans = 10 - (X // 200)

    # 結果出力
    print(ans)

if __name__ == "__main__":
    # 標準入力を取得
    X = get_input()

    # メイン処理
    main(X)
