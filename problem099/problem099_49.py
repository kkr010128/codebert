import math

M=list(map(int, input().split()))
N=M[0]
K=M[1]

A=list(map(int, input().split()))

def cancut(A,N,K,X): #A1..ANをK回で全てX以下に切れるか？Yesなら1、Noなら2を返す。
    cut=0
    for a in A:
        n = (a + X - 1) // X  # a/x の少数切上げ
        cut += n - 1
    if cut<=K:
        return 1
    else:
        return 0

left=0
right=max(A)

while(abs(right - left) > 1):
    mid=(right+left)//2
    if cancut(A,N,K,mid)==1:
        right=mid
    else:
        left=mid

print(right)