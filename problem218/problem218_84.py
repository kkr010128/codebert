from collections import Counter as Ct
INT = lambda: int(input())
INTM = lambda: map(int,input().split())
STRM = lambda: map(str,input().split())
STR = lambda: str(input())
LIST = lambda: list(map(int,input().split()))
LISTS = lambda: list(map(str,input().split()))

def do():
    n=INT()
    dic=[]
    for i in range(n):
        s=STR()
        dic.append(s)
    ctd=Ct(dic)
    ctm=max(ctd.values())
    ans=[]
    for key,value in ctd.items():
        if value==ctm:
            ans.append(key)
    
    ans=sorted(ans)

    for i in ans:
        print(i)


if __name__=='__main__':
    do()