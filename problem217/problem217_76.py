N=input()
A=input()
Alist=A.split()
counts=0
for i in Alist:
    if int(i)%2==1:
        counts=counts
    elif int(i)%3==0:
        counts=counts
    elif int(i)%5==0:
        counts=counts
    else:
        counts=counts+1
if counts>=1:
    print("DENIED")
else:
    print("APPROVED")