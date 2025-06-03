def main():
    N, K = map(int, input().split())
    *A, = map(int, input().split())

    ans = []
    for i in range(K, N):
        cond = A[i] > A[i - K]
        ans.append('Yes' if cond else 'No')

    print(*ans, sep='\n')


if __name__ == '__main__':
    main()
