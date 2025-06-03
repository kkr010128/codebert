def main():
    N, M = map(int, input().split())
    *A, = map(int, input().split())

    A.sort(reverse=True)

    tot = sum(A)

    cond = A[M - 1] * 4 * M >= tot

    print('Yes' if cond else 'No')


if __name__ == '__main__':
    main()
