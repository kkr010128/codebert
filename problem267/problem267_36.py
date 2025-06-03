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
        N (int): 桁数
        S (str): ラッキーナンバー
    """
    # 求解処理
    ans = 0
    x_bit = [False for n in range(10)]
    for x in range(N):
        S_x = int(S[x])
        if x_bit[S_x]:
            continue
        x_bit[S_x] = True
        y_bit = [False for n in range(10)]
        for y in range(x + 1, N):
            S_y = int(S[y])
            if y_bit[S_y]:
                continue
            y_bit[S_y] = True
            z_bit = [False for n in range(10)]
            for z in range(y + 1, N):
                S_z = int(S[z])
                if z_bit[S_z]:
                    continue
                z_bit[S_z] = True
                ans += 1

    # 結果出力
    print(ans)


if __name__ == "__main__":
    # 標準入力を取得
    N, S = get_input()

    # メイン処理
    main(N, S)
