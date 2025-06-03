import sys
input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))

    A = sorted(A)
    ans = 0
    for i in range(1, N):
        ans += A[N - (i // 2) -1]

    
    print(ans)

main()