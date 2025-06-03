
N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def isok(bs, RT):
    return True if bs <= RT else False

def search(B, RT):
    left = -1
    right = M+1
    while right-left>1:
        mid = left+(right-left)//2
        if isok(B[mid], RT):
            left = mid
        else:
            right = mid
    return left

def solve():
    asum = [0]*(N+1)
    bsum = [0]*(M+1)
    for i in range(N):
        asum[i+1]=asum[i]+A[i]
    for i in range(M):
        bsum[i+1]=bsum[i]+B[i]

    ans = 0
    for i in range(N+1):
        RT = K-asum[i]
        if RT < 0:
            break
        ans = max(ans, i+search(bsum, RT))
    print(ans)


if __name__ == '__main__':
    solve()
