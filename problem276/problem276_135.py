def main():
    N=int(input())
    A=[int(_) for _ in input().split()]
    left=0
    right=sum(A)
    ans=right
    for i in range(N):
        left+=A[i]
        right-=A[i]
        ans = min(ans, abs(left-right))
    print(ans)

main()