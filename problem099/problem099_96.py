def General_Binary_Search(L,R,cond,Integer=True,ep=1/(1<<20)):
    """一般的な二部探索を行う.
    L:解の下限
    R:解の上限
    cond:条件(1変数関数,単調減少を満たす)
    Integer:解を整数に制限するか?
    ep:Integer=Falseのとき,解の許容する誤差
    """

    if Integer:
        R+=1
        while R-L>1:
            C=L+(R-L)//2
            if cond(C):
                L=C
            else:
                R=C
        return L
    else:
        C=(R-L)/2
        while (R-C)>ep:
            if cond(C):
                L=C
            else:
                R=C
            C=L+(R-L)/2
        return C
#======================================
N,K=map(int,input().split())
A=list(map(int,input().split()))

def f(x):
    r=0
    for a in A:
        r+=(a+x-1)//x
    return r-N

print(-General_Binary_Search(-max(A),-1,lambda x:f(-x)<=K))