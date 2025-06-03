
def solve():
    n=int(input())
    a=list(map(int,input().split()))
    cnt=[0]*(int(1e5)+9)
    s=0
    for i in range(0,n) :
        s+=a[i]
        cnt[a[i]]+=1
    q=int(input())
    for q in range(0,q) :
        b,c=map(int,input().split())
        ct=cnt[b]
        s+=ct*(c-b)
        cnt[b]=0
        cnt[c]+=ct
        print(s)

solve()
