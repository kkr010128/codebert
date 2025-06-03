# でつoO(YOU PLAY WITH THE CARDS YOU'RE DEALT..)
import sys
def main(N, K, A, F):
    A.sort()
    F.sort(reverse=True)

    def f(x):
        sy = 0
        for a, f in zip(A, F):
            m = a * f
            if m > x:
                sy += (m - x + f - 1) // f
        return sy

    under = -1
    hi = 10**12 + 1
    while hi - under > 1:
        m = (hi + under) // 2
        if f(m) <= K: hi = m
        else: under = m
    print(hi)

if __name__ == '__main__':
    input = sys.stdin.readline
    N, K = map(int, input().split())
    *A, = map(int, input().split())
    *F, = map(int, input().split())
    main(N, K, A, F)
