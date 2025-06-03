import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    a=LI()
    ALL=0
    for i in range(N):
        ALL=ALL^a[i]
        
    ans=[0]*N
    for i in range(N):
        ans[i]=ALL^a[i]
        
    print(' '.join(map(str, ans)))

main()
