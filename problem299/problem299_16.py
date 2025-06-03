import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    A=LI()
    L=[]
    for i in range(N):
        L.append([A[i],i])
        
    L.sort()
    ans=[]
    for i in range(N):
        ans.append(L[i][1]+1)
        
    print(' '.join(map(str, ans)))

main()
