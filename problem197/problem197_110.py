import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    a,b,c = LI()
    ans = 4*a*b<(c-a-b)**2 and c-a-b>0
    print("Yes" if ans else "No")
main()            
