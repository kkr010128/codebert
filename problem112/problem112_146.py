import sys
import heapq

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N, K = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]

    MOD = 10 ** 9 + 7

    plus = []
    minus = []
    for a in A:
        if a >= 0:
            heapq.heappush(plus, -a)
        else:
            heapq.heappush(minus, a)

    ans = 1

    # 絶対マイナスになる場合
    if len(plus) < K - min((K - K % 2), (len(minus) - len(minus) % 2)):
        plus = []
        minus = []
        for a in A:
            if a >= 0:
                heapq.heappush(plus, a)
            else:
                heapq.heappush(minus, -a)

        while K > 0:
            if plus:
                x = plus[0]
            else:
                x = float("inf")

            if minus:
                y = -minus[0]
            else:
                y = float("inf")

            if abs(x) <= abs(y):
                ans *= x
                if plus:
                    heapq.heappop(plus)
            else:
                ans *= y
                if minus:
                    heapq.heappop(minus)

            ans %= MOD
            K -= 1

        print(ans)

    else:
        while K > 0:
            if K >= 2 and len(minus) >= 2 and len(plus) >= 2:
                x1 = plus[0]
                x2 = plus[1]
                y1 = minus[0]
                y2 = minus[1]
                if x1 * x2 <= y1 * y2:
                    y1 = heapq.heappop(minus)
                    y2 = heapq.heappop(minus)
                    ans *= (y1 * y2)
                    ans %= MOD
                    K -= 2
                else:
                    x1 = -heapq.heappop(plus)
                    ans *= x1
                    ans %= MOD
                    K -= 1
            elif K >= 2 and len(minus) >= 2:
                y1 = heapq.heappop(minus)
                y2 = heapq.heappop(minus)
                ans *= (y1 * y2)
                ans %= MOD
                K -= 2
            else:
                x = -heapq.heappop(plus)
                ans *= x
                ans %= MOD
                K -= 1

        print(ans % MOD)


if __name__ == '__main__':
    main()
