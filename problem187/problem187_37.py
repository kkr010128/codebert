import sys
from collections import defaultdict
# from collections import Counter
# from queue import PriorityQueue
# sys.setrecursionlimit(2000000)

def distance(X, Y, start, goal):
    ans = float('inf')

    tmp = goal - start
    if tmp < ans:
        ans = tmp

    # start ~ X ~ Y ~ goal,
    tmp = abs(X - start) + 1 + abs(goal - Y)
    if tmp < ans:
        ans = tmp

    # start ~ Y ~ X ~ goal
    tmp = abs(Y - start) + 1 + abs(goal - X)
    if tmp < ans:
        ans = tmp

    return ans

#     # 短絡パスを使える場合
#     if start <= X and Y <= goal

#     # 短絡パスを使えないならば、普通に距離を計算
#     if X < start:
#         return goal - start

#     # 短絡パスを使えても、隣のパスへの距離は1
#     if goal - start == 1:
#         return 1

#     # 短絡パスより手前だと使えない
#     if goal < Y:
#         return goal - start



    # return goal - start - 1

def main():
    # N = int(input())

    N, X, Y = [int(s) for s in input().split()]

    distance_dict = defaultdict(int)
    for i in range(1, N+1):
        for j in range(i + 1, N+1):
            d = distance(X, Y, i, j)
            # sys.stderr.write('{} to {} : d = {}\n'.format(i, j, d))
            # ditance_dict[(i, j)] = d
            distance_dict[d] += 1

    for k in range(1, N):
        # print(str(distance_dict[k]))
        print(distance_dict[k])

    # As = []
    # Bs = []
    # for i in range(N):
    #     A, B = [int(s) for s in input().split()]
    #     As.append(A)
    #     Bs.append(B)

    return 0

if __name__ == '__main__':
    sys.exit(main())
