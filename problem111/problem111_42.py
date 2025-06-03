def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int,input().split()))
    A.sort(reverse=True)
    ans = A[0]
    for i in range(2,N):
        ans += A[i//2]
    print(ans)


if __name__ == '__main__':
    main()
