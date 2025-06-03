S=input()
Q=int(input())
p=0
u=0
l=""
r=""
for i in range(Q):
    q=list(input().split())
    if q[0]=="1":
        u+=1
    else:
        if q[1]=="1" and u%2==0 or q[1]=="2" and u%2==1:
            l=l+q[2]
        else:
            r=r+q[2]
if u%2==0:
    l=l[::-1]
    S=l+S+r
else:
    S=S[::-1]
    r=r[::-1]
    S=r+S+l
print(S)
