def solve():
    A,B,C,K = [int(i) for i in input().split()]
    ans = 0
    ans += min(A, K)
    if K-A-B > 0:
        ans -= (K-A-B)
    print(ans)

if __name__ == "__main__":
    solve()