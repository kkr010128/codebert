import sys
input = sys.stdin.buffer.readline

def main():
    N, K = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    l, r = 0, N-1
    MOD = 10**9+7
    if K == N:
        ans = 1
        for num in A:
            ans *= num
            ans %= MOD
        print(ans)
        exit()
    elif A[-1] < 0 and K%2 == 1:
        ans = 1
        for i in range(K):
            ans *= A[-i-1]
            ans %= MOD
        print(ans)
        exit()
    ans = 1
    if K%2 == 1:
        ans *= A[-1]
        r -= 1
    for _ in range(K//2):
        nl = A[l]*A[l+1]
        nr = A[r]*A[r-1]
        if nl > nr:
            ans *= nl
            l += 2
        else:
            ans *= nr
            r -= 2
        ans %= MOD
    print(ans)

if __name__ == "__main__":
    main()
