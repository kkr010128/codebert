# でつoO(YOU PLAY WITH THE CARDS YOU'RE DEALT..)
import sys
def main(N, M, S):
    ans = []
    i = N
    while i > 0:
        for j in range(max(0, i - M), i):
            if S[j] == '0':
                ans.append(i - j)
                i = j
                break
        else:
            print(-1)
            return
    print(*list(reversed(ans)))

if __name__ == '__main__':
    input = sys.stdin.readline
    N, M = map(int, input().split())
    S = input().rstrip()
    main(N, M, S)
