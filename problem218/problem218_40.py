
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    from collections import defaultdict
    dd = defaultdict(int)
    
    N=I()
    M=0
    for i in range(N):
        s=input()
        dd[s]+=1
        M=max(M,dd[s])
        
        
    ans=[]
    for k,v in dd.items():
        if v==M:
            ans.append(k)
            
    ans.sort()
    for k in ans:
        print(k)
        
    

main()
