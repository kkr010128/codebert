def solve_knapsack_problem(A,n,m):
    a=[[0 for i in range(m+1)]for j in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if A[i-1]<=j:
                a[i][j] = max(a[i-1][j-A[i-1]]+A[i-1],a[i-1][j])
            else:
               a[i][j] = a[i-1][j]
            
            if a[i][j] == m:
                return True
    return False

if __name__ == "__main__":
    n=int(input())
    A=list(map(int,input().split()))
    q=int(input())
    m=list(map(int,input().split()))
    result=[]

    for i in range(q):
        if solve_knapsack_problem(A,n,m[i]):
            print("yes")
        else:
            print("no")
                    

