import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    S = input().strip("\n")
    Left = [set() for _ in range(N)]
    Right = [set() for _ in range(N)]
    Left[0] |= {S[0]}
    Right[N-1] |= {S[N-1]}
    for i in range(1, N):
        Left[i] = Left[i-1] | {S[i]}
        Right[N-i-1] = Right[N-i] | {S[N-i-1]}
    used = set()
    for i in range(1, N - 1):
        mid = S[i]
        for l in Left[i-1]:
            for r in Right[i+1]:
                used |= {l + mid + r}
    print(len(used))

    return 0

if __name__ == "__main__":
    solve()