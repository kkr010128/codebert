import sys
sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline


def main():
    t1, t2 = map(int, input().split())
    a1, a2 = map(int, input().split())
    b1, b2 = map(int, input().split())

    P = t1 * (b1 - a1)
    Q = t2 * (b2 - a2)
    if P + Q == 0:
        print("infinity")
        return
    if P * (P + Q) > 0:
        print(0)
        return
    P = abs(P)
    Q = abs(Q)
    T = P % (Q - P)
    S = P // (Q - P)
    if T == 0:
        ans = 2 * S
    else:
        ans = 2 * S + 1
    print(ans)


main()
