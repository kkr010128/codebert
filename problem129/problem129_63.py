def main(): 
    n = int(input())
    A = list(map(int,input().split()))

    ans = n
    A.sort()
    table = [True]*(A[-1]+1)
    for k,a in enumerate(A):
        if table[a]:
            if k+1<n and A[k+1]==a:
                ans-=1
            for i in range(a,A[-1]+1,a):
                table[i] = False
        else:
            ans-=1
    
    print(ans)
main()