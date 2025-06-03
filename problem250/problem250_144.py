INT = lambda: int(input())
INTM = lambda: map(int,input().split())
STRM = lambda: map(str,input().split())
STR = lambda: str(input())
LIST = lambda: list(map(int,input().split()))
LISTS = lambda: list(map(str,input().split()))
def do():
    x=INT()
    for i in range(x,100004):
        flg=1
        lim=int(x**0.5+1)
        for k in range(2,lim):
            if i%k==0:
                flg=0
                break
        if flg==1:
            print(i)
            break
if __name__ == '__main__':
    do()