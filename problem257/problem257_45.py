import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    A=LI()
    cnt=0
    now=1
    
    for i in range(N):
        if A[i]==now:
            now+=1
        else:
            cnt+=1
            
    if cnt==N:
        cnt=-1
    print(cnt)
        

main()
