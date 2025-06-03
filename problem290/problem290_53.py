# coding: utf-8
# Your code here!
#一時保存
def count(target):
    num=0
    for i in range(N):
        temp=target//F[i]
        num+=max(A[i]-temp,0)
    return num

N,K=map(int,input().split())

A=list(map(int,input().split()))
F=list(map(int,input().split()))

A.sort()
F.sort(reverse=True)


ok=10**16+1
ng=0

if count(0)<=K:
    print(0)
    exit()


while ok-ng>1:
    mid=(ok+ng)//2
    if count(mid)>K:
        ng=mid
    else:
        ok=mid
ng=0
while ok-ng>1:
    mid=(ok+ng)//2
    if count(mid)>K:
        ng=mid
    else:
        ok=mid


print(ok)

