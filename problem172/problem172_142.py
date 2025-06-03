A=list(map(int,input()))
b=0

for i in range(0,3):
    if A[i]==7:
        b+=1

if b==0:
    print("No")
else:
    print("Yes")