N=int(input())
D=[]
TF=[]
for i in range(N):
    Input=list(map(int,input().split()))
    D.append(Input)
    if D[i][0]==D[i][1]:
        TF.append(1)
    else:
        TF.append(0)
TF.append(0)
TF.append(0)
Q=[]
for i in range(N):
    temp=TF[i]+TF[i+1]+TF[i+2]
    Q.append(temp)
if max(Q)==3:
    print("Yes")
else:
    print("No")