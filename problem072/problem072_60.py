N=int(input())
count=0
a=0
for i in range(N):
    D=list(map(int,input().split()))
    if D[0]==D[1]:
        count+=1
        if count>=3:
            a=1
            break
    else:
        count=0
if a==1:
    print("Yes")
else:
    print("No")