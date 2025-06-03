S=input()
Q=int(input())
A=[list(input().split()) for i in range(Q)]
c=0
R=""
L=""
for i in range(Q):
    if A[i][0]=="1":
        c+=1
        continue
    if c%2==1 and A[i][0]=="2":
        if A[i][1]=="1":
            R=R+A[i][2]
        elif A[i][1]=="2":
            L=A[i][2]+L
    elif c%2==0 and A[i][0]=="2":
        if A[i][1]=="1":
            L=A[i][2]+L
        elif A[i][1]=="2":
            R=R+A[i][2]
S=L+S+R
if c%2==1:
    S=S[::-1]
print(S)