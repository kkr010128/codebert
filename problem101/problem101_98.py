a,b,c=map(int,input().split())
k=int(input())
while k>0:
    if a<b:
        break
    b*=2
    k-=1
while k>0:
    if b<c:
        break
    c*=2
    k-=1
if a<b<c:
    print('Yes')
else:
    print('No')