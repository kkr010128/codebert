# -*- coding: utf-8 -*-

def get_input() -> str:
    """
    標準入力を取得する.

    Returns:\n
        str: 標準入力
    """
    S = input()

    return S


def main(S: str) -> None:
    """
    メイン処理.

    Args:\n
        S (str): 文字列(1 <= |S| <= 1000, 英子文字のみ)
    """
    # 求解処理
    ans = S
    if S[-1] == "s":
        ans += "es"
    else:
        ans += "s"

    # 結果出力
    print(ans)


if __name__ == "__main__":
    # 標準入力を取得
    S = get_input()

    # メイン処理
    main(S)
