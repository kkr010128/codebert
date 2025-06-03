INT = lambda: int(input())
INTM = lambda: map(int,input().split())
STRM = lambda: map(str,input().split())
STR = lambda: str(input())
LIST = lambda: list(map(int,input().split()))
LISTS = lambda: list(map(str,input().split()))

def do():
    n=INT()
    p=LIST()
    tm=10**9
    ct=0
    for i in range(n):
        if tm>=p[i]:
            ct+=1
        tm=min(tm,p[i])
    print(ct)

if __name__=='__main__':
    do()