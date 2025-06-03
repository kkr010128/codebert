import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    X=LI()
    
    ans=10**10
    
    for i in range(1,101):
        temp=0
        for j in range(N):
            temp+=abs(i-X[j])**2
        ans=min(ans,temp)
        
    print(ans)
        

main()
