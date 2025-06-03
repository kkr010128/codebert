
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,M=MI()
    S=list(input())
    S2=S[::-1]
    
    now=0
    ans=[]
    while now!=N:
        nxt=now+M
        if nxt>N:
            nxt=N
        while S2[nxt]=="1":
            nxt-=1
        if now==nxt:
            ans=[-1]
            break
        ans.append(nxt-now)
        now=nxt
        
    print(' '.join(map(str, ans[::-1])))
    
main()
