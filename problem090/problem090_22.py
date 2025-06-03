Q =input()
if Q.count('R')==3:
    print(3)
elif Q.count('R')==0:
    print(0)
elif Q.count('R')==1:
    print(1)
elif Q.count('R')==2:
    if Q[1] =='S':
        print(1)
    else :
        print(2)