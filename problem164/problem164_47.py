d_pre=input().split()
d=[int(s) for s in d_pre]
A=d[0]
B=d[1]
C=d[2]
D=d[3]
for i in range(210):
    if i%2==0:
        C-=B
        if C<=0:
            print("Yes")
            break
    else:
        A-=D
        if A<=0:
            print("No")
            break