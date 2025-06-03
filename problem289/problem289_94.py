import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    a,b,x = LI()
    ans = 0

    if x >= a**2 * b/2:
        ans = math.degrees(math.atan((a**2*b-x)*2/a**3))
    else:
        ans = math.degrees(math.atan(a*b**2/(2*x)))
    
    print(ans)
main()
