#!/usr/bin/env python
"""NOMURA プログラミングコンテスト 2020: C - Folia
https://atcoder.jp/contests/nomura2020/tasks/nomura2020_c
"""


def main():
    N = int(input())
    As = list(map(int, input().split()))

    leaves_count = sum(As)
    node_count = 1
    ans = 0
    for i, a in enumerate(As):
        leaves_count -= a
        next_node_count = min(leaves_count, (node_count - a) * 2)
        if next_node_count < 0:
            ans = -1
            break
        ans += node_count
        node_count = next_node_count

    print(ans)


if __name__ == '__main__':
    main()
