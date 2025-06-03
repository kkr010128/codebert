# -*- coding: utf-8 -*-

def get_input() -> tuple:
    """
    標準入力を取得する.

    Returns:\n
        tuple: 標準入力
    """
    N = int(input())
    S = input()

    return N, S


def main(N: int, S: str) -> None:
    """
    メイン処理.

    Args:\n
        N (int): 桁数(4 <= N <= 30000)
        S (str): ラッキーナンバー(半角数字からなる長さNの文字列)
    """
    # 求解処理
    ans = 0
    S_i_list = []
    for i in range(N - 2):
        S_i = S[i]
        if S_i in S_i_list:
            continue
        S_j_list = []
        for j in range(i + 1, N - 1):
            S_j = S[j]
            if S_j in S_j_list:
                continue
            ans += len(set(S[j + 1: N]))
            S_j_list.append(S_j)
        S_i_list.append(S_i)

    # 結果出力
    print(ans)


if __name__ == "__main__":
    # 標準入力を取得
    N, S = get_input()

    # メイン処理
    main(N, S)
