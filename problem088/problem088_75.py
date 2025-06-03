def main():
    N, A = int(input()), list(map(int, input().split()))

    ans = 0
    for idx in range(1, N):
        if A[idx] < A[idx - 1]:
            diff = A[idx - 1] - A[idx]
            ans += diff 
            A[idx] = A[idx - 1]

    print('{}'.format(ans))

if __name__ == '__main__':
    main()
