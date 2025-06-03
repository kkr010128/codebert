
def main():
    pass
    N = int(input())
    A = list(map(int, input().split()))

    H = [0]*N
    for i in range(0,N):
        if i >= A[i]:
            H[i-A[i]] += 1

    ans = 0
    for k in range(0,N):
        Bk = k+A[k]
        if Bk < N:
            ans += H[Bk]

    print(ans)

if __name__ == '__main__':
    main()
