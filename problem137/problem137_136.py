def main():
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = (int(i) for i in input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    ans = -1
    if N % 2 == 1:
        ans = B[N//2] - A[N//2] + 1
    else:
        a = (A[N//2] + A[N//2 - 1])/2
        b = (B[N//2] + B[N//2 - 1])/2
        ans = b - a + 1
        ans += ans - 1
    print(int(ans))


if __name__ == '__main__':
    main()
