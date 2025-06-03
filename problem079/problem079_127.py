import sys
N = int(input())
if N>=4:
    C=[0]*N
    C[0]=0
    C[1]=0
    C[2]=1
    n=2
    #フィボナッチ数列のイメージ
    while True:
        n=n+1
        C[n]=C[n-1]+C[n-3]
        #print(n,C[n])
        if n==(N-1):
            break
    print(C[N-1]%(10**9+7))
if N==3:
    print(1)
if N<=2:
    print(0)