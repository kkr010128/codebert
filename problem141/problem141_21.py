import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

N = int(input())
A = list(map(int, input().split()))

import math

# 葉から調査し、範囲を求める
limits = [(A[-1], A[-1])]
# for i in reversed(range(0, len(A)-1)):
for i in reversed(range(0, N)):
    min_ = math.ceil(limits[-1][0] / 2)
    max_ = limits[-1][1]
    # print("min_ {} max_ {} leaf {}".format(min_, max_, A[i]))
    limits.append((min_ + A[i], max_ + A[i]))
# print("limits: {}".format(limits))
if limits[-1][0] != 1:
    print(-1)
    quit()

# 根からにする
limits.reverse()

# 根から制約に基づき最大値を計算する
tree = [1]
for i in range(1, N+1):
    nodes = min(2 * (tree[-1] - A[i-1]), limits[i][1])
    tree.append(nodes)
# print(limits)
# print(tree)

ans = sum(tree)
print(ans)