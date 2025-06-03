import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    def select(n,k):
        return math.factorial(n)//(math.factorial(k)*math.factorial(n-k))
    n,m = LI()
    ans = 0
    if n>=2:
        ans += n*(n-1)//2
    if m>=2:
        ans += m*(m-1)//2

    print(ans)
main()            
