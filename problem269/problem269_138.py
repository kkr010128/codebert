from sys import stdin
T1,T2 = [int(x) for x in stdin.readline().rstrip().split()]
A1,A2 = [int(x) for x in stdin.readline().rstrip().split()]
B1,B2 = [int(x) for x in stdin.readline().rstrip().split()]
f = (A1-B1)*T1
s = (A2-B2)*T2
 
if f + s == 0:
    print("infinity")

else:
    if (f > 0) and ((f + s) > 0):
        print(0)
    
    elif (f < 0) and ((f + s) < 0):
        print(0)
        
    elif f > 0 and f + s < 0:
        if  f % (-(f + s)) == 0:
            print((f//-(f+s))*2)
        else:
            print((f//-(f+s))*2+1)
    
    elif f < 0 and f + s > 0:
        if (-f) % (f+s) == 0:
            print((-f//(f+s))*2)
        else:
            print((-f//(f+s))*2+1)