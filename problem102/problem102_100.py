# -*- coding: utf-8 -*-

def get_input() -> tuple:
    """
    標準入力を取得する.

    Returns:\n
        tuple: 標準入力
    """
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))

    return N, K, A

def main(N: int, K: int, A: list) -> None:
    """
    メイン処理.

    Args:\n
        N (int): 学期数（2 <= N <= 200000）
        K (int): 直近何回分までの点数を考慮するか（1 <= K <= N - 1）
        A (list): i学期の期末テストの点数
    """
    # 求解処理
    for i in range(K, N):
        if A[i] > A[i - K]:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    # 標準入力を取得
    N, K, A = get_input()

    # メイン処理
    main(N, K, A)
