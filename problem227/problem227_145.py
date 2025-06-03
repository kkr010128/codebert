import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,K=MI()
    h=LI()
    
    h.sort()
    
    if K>=N:
        print(0)
        exit()
        
    for i in range(K):
        h[-1-i]=0
        
    ans=sum(h)
    print(ans)

main()
