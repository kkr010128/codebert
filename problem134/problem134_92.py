def solve(N,A) :
    ans = 1
    for i in range(N) :
        if(A[i] == 0) :
            print(0)
            return
    for i in range(N) :
        ans = ans * A[i]
        if(ans > 10**18):
            ans = -1
            break
    print(ans)
    
N = int(input())
A = list(map(int, input().split()))
solve(N,A)