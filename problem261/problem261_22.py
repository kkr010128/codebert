import sys
input = sys.stdin.readline


def read():
    S = input().strip()
    return S,


def solve(S):
    N = len(S)
    ans = 0
    for i in range(N//2):
        if S[i] != S[N-i-1]:
            ans += 1
    return ans


if __name__ == '__main__':
    inputs = read()
    print(solve(*inputs))
