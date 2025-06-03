def main():
    n = int(input().strip())
    L = list(map(int, input().strip().split()))
    
    rem=sum(L)
    cur=1
    ans=0
    for i in range(n+1):
        ans+=cur
        rem-=L[i]
        cur-=L[i]
        if cur<0 or cur==0 and i!=n:
            print(-1)
            return
        if cur<rem:
            cur=min(cur*2,rem)
            
    print(ans)

if '__main__' == __name__:
    main()
