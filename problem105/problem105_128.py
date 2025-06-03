def main():
    N = int(input())
    *A, = map(int, input().split())
    ans = sum(A[i] & 1 for i in range(0, N, 2))
    print(ans)


if __name__ == '__main__':
    main()
