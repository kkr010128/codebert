def Binary_Search_Count(A,x,sort=True,equal=False):
    """2分探索によって,x未満の要素の個数を調べる.

    A:リスト
    x:調べる要素
    sort:ソートをする必要があるかどうか(Trueで必要)
    equal:Trueのときはx"未満"がx"以下"になる
    """
    if sort:
        A.sort()
        
    N=len(A)
    if A[-1]<=x:
        return N
    elif x<A[0] or (not equal and x==A[0]):
        return 0

    L,R=0,N
    while R-L>1:
        C=L+(R-L)//2
        if x<A[C] or (not equal and x==A[C]):
            R=C
        else:
            L=C
    return R

def Binary_Search_High_Value(A,x,sort=True,equal=False):
    """Aのxを超える要素の中で最小のものを出力する.

    A:リスト
    x:調べる要素
    sort:ソートをする必要があるかどうか(Trueで必要)
    equal:Trueのときはx"を超える"がx"以上"になる
    ※全ての要素がx以下(未満)場合はNoneが返される.
    """
    
    if sort:
        A.sort()

    K=Binary_Search_Count(A,x,sort=False,equal=not equal)
    if K==len(A):
        return None
    else:
        return A[K]

N=int(input())
T={i:[] for i in range(10)}

S=input()
for i in range(N):
    T[int(S[i])].append(i)

X=0
for k in range(10**3):
    a,b,c=(k//100),(k//10)%10,k%10

    if T[a]:
        x=T[a][0]
        if T[b]:
            y=Binary_Search_High_Value(T[b],x,False,False)
            if y!=None and T[c]:
                z=Binary_Search_High_Value(T[c],y,False,False)
                if z!=None:
                    X+=1
print(X)
