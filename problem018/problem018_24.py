#ALDS1_3-A Elementary data structures - Stack
A=input().split()
while(len(A)>1):
    for i in range(len(A)):
        if(A[i]=="+"):
            A[i]=int(A[i-2])+int(A[i-1])
            A=A[:i-2]+A[i:]
            break
        elif(A[i]=="-"):
            A[i]=int(A[i-2])-int(A[i-1])
            A=A[:i-2]+A[i:]
            break
        elif(A[i]=="*"):
            A[i]=int(A[i-2])*int(A[i-1])
            A=A[:i-2]+A[i:]
            break
print(A[0])