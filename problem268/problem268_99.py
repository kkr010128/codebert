
def resolve():
    MOD = 1000000007
    N = int(input())
    A = list(map(int, input().split()))

    C = [0]*(N+1)
    C[0] = 3
    ans = 1
    for i in range(N):
        a = A[i]
        ans *= C[a]
        ans %= MOD
        C[a] -= 1
        C[a+1] += 1

    print(ans)
    
if __name__ == "__main__":
    resolve()