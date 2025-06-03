import sys
import math


def input():
    return sys.stdin.readline().rstrip()


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    ng = 0
    ok = 10 ** 9 + 1

    while ok - ng > 1:
        mid = (ok + ng) // 2
        ans = sum(list(map(lambda x: math.ceil(x / mid) - 1, A)))

        # for i in range(N):
        #     ans += A[i]//mid -1
        #     if A[i]%mid !=0:
        #         ans +=1

        if ans <= K:
            ok = mid
        else:
            ng = mid

    print(ok)


if __name__ == "__main__":
    main()
