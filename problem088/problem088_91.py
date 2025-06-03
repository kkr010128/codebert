def main() :
    N = int(input())
    A = list(map(int, input().split()))
    sum = 0
    t = A[0]
    for i in range(1, N):
        if A[i] <= t:
            sum += t - A[i]
        else:
            t = A[i]
    print(sum)


if __name__ == "__main__":
    main()