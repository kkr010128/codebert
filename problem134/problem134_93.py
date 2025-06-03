def solve():
    N = int(input())
    A = [int(i) for i in input().split()]
    ans = 1
    for i in range(N):
        if ans == -1 and A[i] != 0:
            continue
        ans *= A[i]
        if ans > 10**18:
            ans = -1
    print(ans)

if __name__ == "__main__":
    solve()