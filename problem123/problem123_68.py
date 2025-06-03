import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n = I()
    a = LI()

    acc = 0
    for i in a:
        acc ^= i
    
    ans_lst = []
    for i in a:
        ans = acc^i
        ans_lst.append(ans)

    print(*ans_lst)
main()
