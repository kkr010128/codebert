# でつoO(YOU PLAY WITH THE CARDS YOU'RE DEALT..)
import sys
INF = -1
def main(T1, T2, A1, A2, B1, B2):
    D1 = T1 * (A1 - B1)
    D2 = D1 + T2 * (A2 - B2)

    if D1 * D2 > 0:
        return 0

    if abs(D1) == abs(D2) or D2 == 0:
        return INF

    d, m = divmod(abs(D1), abs(D2))
    return (1 if m else 0) + 2 * d


if __name__ == '__main__':
    input = sys.stdin.readline
    T1, T2 = map(int, input().split())
    A1, A2 = map(int, input().split())
    B1, B2 = map(int, input().split())
    ans = main(T1, T2, A1, A2, B1, B2)
    print(ans if ans >= 0 else 'infinity')
