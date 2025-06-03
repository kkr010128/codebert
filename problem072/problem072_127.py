import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    cnt=0
    flag=0
    for _ in range(N):
        a,b=MI()
        if a==b:
            cnt+=1
        else:
            cnt=0
            
        if cnt==3:
            flag=1
            break
        
    if flag==1:
        print("Yes")
    else:
        print("No")

main()
