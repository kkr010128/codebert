'''
A[i]<A[j]
F[i]<F[j]
となる組み合わせが存在したと仮定

max(A[i]*F[i],A[j]*F[j])=A[j]*F[j]
>A[i]*F[j]
>A[j]*F[i]
より、この場合はiとjを入れ替えたほうが最適となる。

結局
Aを昇順ソート
Fを降順ソート
するのが最適となる。
問題は修行の割当である。
順序を保ったまま修行していっても問題ない
3,2->1,2と
3.2->2,1は同じとみなせるため
二分探索
成績をmidにするために必要な修行コスト
lowならK回より真に大
highならK回以下
'''
N,K=map(int,input().split())
A=[int(i) for i in input().split()]
F=[int(i) for i in input().split()]
A.sort()
F.sort(reverse=True)
low=-1
high=max(A)*max(F)+1
while(high-low>1):
    mid=(high+low)//2
    tmp=0
    for i in range(N):
        #A[i]*F[i]-mid<=X*F[i]
        x=(A[i]*F[i]-mid+F[i]-1)//F[i]
        if x<0:
            continue
        tmp+=x
    if tmp<=K:
        high=mid
    else:
        low=mid
print(high)
