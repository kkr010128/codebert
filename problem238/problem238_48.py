def main():
    N, K, S = (int(i) for i in input().split())
    if S == 10**9:
        A = [S]*K + [1]*(N-K)
    else:
        A = [S]*K + [10**9]*(N-K)
    print(*A)


if __name__ == '__main__':
    main()
