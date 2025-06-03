# でつoO(YOU PLAY WITH THE CARDS YOU'RE DEALT..)
import sys
def main(N, A):
    C = [0] * (10**6 + 1)
    for a in A:
        if C[a] == 1:
            C[a] = -1
            continue
        if C[a] == -1:
            continue
        C[a] = 1
        for b in range(a + a, 10 ** 6 + 1, a):
            C[b] = -1
    ans = 0
    for a in A:
        if C[a] == 1:
            ans += 1
    print(ans)

if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())
    *A, = map(int, input().split())
    main(N, A)
