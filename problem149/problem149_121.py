import sys
input = sys.stdin.readline

def main():
    N, M, X = map(int, input().split())
    ca = [list(map(int, input().split())) for _ in range(N)]

    ans = sys.maxsize
    for mask in range(2 ** N):
        C = 0
        A = [0] * N
        for i in range(N):
            if ((mask >> i) & 1):
                C += ca[i][0]
                A = [a + c for a, c in zip(A, ca[i][1:])]
        if all([i >= X for i in A]):
            ans = min(ans, C)
    if ans != sys.maxsize:
        print(ans)
    else:
        print("-1")

main()