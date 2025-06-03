S = input()

A = S.count("R")
B = S.count("RR")

if A==2:
    if B==1:
        print(2)
    if B==0:
        print(1)

elif  A==1:
    print(1)

elif A==3:
    print(3)
else :
    print(0)