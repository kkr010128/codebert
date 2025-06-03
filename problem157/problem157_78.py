def Binary_Search_Small_Count(A,x,equal=False,sort=False):
    """2分探索によって,x未満の要素の個数を調べる.

    A:リスト
    x:調べる要素
    sort:ソートをする必要があるかどうか(Trueで必要)
    equal:Trueのときはx"未満"がx"以下"になる
    """
    if sort:
        A.sort()

    if A[0]>x or ((not equal) and A[0]==x):
        return 0

    L,R=0,len(A)
    while R-L>1:
        C=L+(R-L)//2
        if A[C]<x or (equal and A[C]==x):
            L=C
        else:
            R=C

    return L+1

def Binary_Search_Equal_Count(A,x,sort=False):
    """2分探索によって,xの個数を調べる.

    A:リスト
    x:調べる要素
    sort:ソートをする必要があるかどうか(Trueで必要)
    equal:Trueのときはx"を超える"がx"以上"になる
    """

    if sort:
        A.sort()

    if x<A[0] or A[-1]<x:
        return 0

    X=Binary_Search_Small_Count(A,x,equal=True)
    Y=Binary_Search_Small_Count(A,x,equal=False)
    return X-Y
#================================================
N=int(input())
A=["*"]+list(map(int,input().split()))

B=[0]*N
for j in range(1,N+1):
    B[j-1]=j-A[j]
B.sort()

K=0
del A[0]
for i in range(1,N+1):
    K+=Binary_Search_Equal_Count(B,i+A[i-1],False)
print(K)
