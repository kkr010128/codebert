A,B,C,D=input().split()
num = 0
while(int(A)>=0 and int(C)>=0):
    if int(A)<= 100 and 0 <= int(B)<= 100 and int(C)<= 100 and 0 <= int(D)<= 100:
        if num %2 == 0:
            C = int(C)-int(B)
            if int(C)<=0:
                print("Yes")
                break
            num += 1
        elif num %2 !=0:
            A = int(A)-int(D)
            if int(A)<=0:
                print("No")
                break
            num += 1
    else:
        break
