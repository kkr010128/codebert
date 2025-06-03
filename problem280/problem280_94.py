INT = lambda: int(input())
INTM = lambda: map(int,input().split())
STRM = lambda: map(str,input().split())
STR = lambda: str(input())
LIST = lambda: list(map(int,input().split()))
LISTS = lambda: list(map(str,input().split()))

import itertools, math

def distance(x1,y1,x2,y2):
    return(((x2-x1)**2+(y2-y1)**2)**0.5)

def do():
    xs=[]
    ys=[]
    per=[]
    n=INT()
    ans=0
    for i in range(n):
        x,y=INTM()
        xs.append(x)
        ys.append(y)
        per.append(i)
    
    for i in itertools.permutations(per, n):
        for k in range(n-1):
            ans+=distance(xs[i[k]],ys[i[k]],xs[i[k+1]],ys[i[k+1]])
        #print(ans)
    
    print(ans/math.factorial(n))

    
if __name__=='__main__':
    do()