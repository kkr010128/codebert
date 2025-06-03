import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n,k = LI()
    p = LI()
    for i,x in enumerate(p):
        if x%2 == 0:
            x = x//2+0.5
        else:
            x = x//2+1
        p[i] = x

    nowsum = sum(p[:k])
    ans = nowsum
    for i in range(k,n):
        nowsum = nowsum - p[i-k] + p[i]
        # print(p,lst)
        ans = max(ans,nowsum)
    
    print(ans)
main()            
