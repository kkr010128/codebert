import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    ans=0
    
    N=I()
    for a in range(1,N):
        for b in range(1,N):
            if a*b>=N:
                break
            ans+=1
            
    print(ans)

        
        
    

main()
