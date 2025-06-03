def main():
    from collections import deque
    N, M = (int(i) for i in input().split())
    if N % 2 == 0:
        A = deque([i+1 for i in range(N)])
        for i in range(1, M+1):
            if (N-i)-i > N//2:
                print(A[i], A[N-i])
            else:
                print(A[i], A[N-i-1])
    else:
        A = deque([i for i in range(N)])
        for i in range(1, M+1):
            print(A[i], A[N-i])


if __name__ == '__main__':
    main()
