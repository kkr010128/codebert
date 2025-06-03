import sys

input = sys.stdin.readline

def main():
    N = int(input())
    P = []
    for i in range(N):
        X, L = map(int, input().split())
        S, T = X-L, X+L
        P.append((S, T))
    P.sort(key=lambda x: x[1])

    ans = 0
    r = -float('inf')
    for s, t in P:
        if s >= r:
            ans += 1
            r = t
    print(ans)

if __name__ == "__main__":
    main()
