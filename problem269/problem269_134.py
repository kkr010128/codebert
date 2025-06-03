import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    T1, T2 = map(int, input().split())
    A1, A2 = map(int, input().split())
    B1, B2 = map(int, input().split())

    P = (A1 - B1) * T1
    Q = (A2 - B2) * T2
    if P > 0:
        P *= -1
        Q *= -1

    if P + Q < 0:
        print(0)
    elif P + Q == 0:
        print("infinity")
    else:
        S = (-P) // (P + Q)
        T = (-P) % (P + Q)
        if T != 0:
            print(S * 2 + 1)
        else:
            print(S * 2)


if __name__ == '__main__':
    resolve()
