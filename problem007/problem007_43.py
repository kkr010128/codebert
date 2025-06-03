A=1
B=1
C=0 #２つ前の項
D=0 #1
N=int(input())
if N==0 or N==1:
    print(1)
elif N==2:
    print(2)

else:   
    C=B  #１
    D=A+B #2
    for i in range (N-3):
        B=C
        C=D
        D=B+C
    print(C+D)
