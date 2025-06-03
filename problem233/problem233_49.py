def main():
    N = int(input())
    *P, = map(int, input().split())

    mi = N + 1
    ret = 0
    for x in P:
        if mi > x:
            mi = x
            ret += 1

    print(ret)


if __name__ == '__main__':
    main()

# import sys
# input = sys.stdin.readline
# 
# sys.setrecursionlimit(10 ** 7)
# 
# (int(x)-1 for x in input().split())
# rstrip()
#
# def binary_search(*, ok, ng, func):
#     while abs(ok - ng) > 1:
#         mid = (ok + ng) // 2
#         if func(mid):
#             ok = mid
#         else:
#             ng = mid
#     return ok
