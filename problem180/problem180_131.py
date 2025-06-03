import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    N,K=mi()
    
    n = N//K
    ans = INF
    for m in [n-1,n,n+1]:
        ans = min(ans,abs(N-K*m))
    print(ans)

if __name__ == "__main__":
    main()