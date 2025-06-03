import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n = I()
    lst = LI()
    cnt = 1
    ans = 0

    for brock in lst:
        if brock == cnt:
            cnt += 1
        else:
            ans += 1

    if cnt != 1:
        print(ans)
    else:
        print(-1)
    
main()
