# -*- coding:utf-8 -*-

def solve():
    import math

    N, K = list(map(int, input().split()))
    As = list(map(int, input().split()))

    left, right = 1, 10**9
    while left != right:
        mid = (left+right)//2
        cut = 0

        for a in As:
            if a/mid > 1: cut += math.ceil(a/mid) - 1

        if cut <= K:
            # 切って良い回数を満たしている
            if left+1 == right:
                print(left)
                return
            right = mid
        else:
            # 切って良い回数を満たしていない
            if left+1 == right:
                print(right)
                return
            left = mid



if __name__ == "__main__":
    solve()
