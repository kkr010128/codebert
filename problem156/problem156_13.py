import sys
X=int(input())
X5=X**0.2
#print('X5=',X5,int(X5))
if X5-int(X5)==0:
    a=int(X5)
    b=0
    print(a,b)
    #print(1)
    sys.exit()
for a in range(1,int(X5)+1):
    for mb in range(a):
        if a**5+mb**5==X:
            print(a,-mb)
            #print(2)
            sys.exit()
for a in range(1,2*int(X5)):
    for b in range(a):
        if a**5-b**5==X:
            print(a,b)
            #print(3)
            sys.exit()
#print(4)
