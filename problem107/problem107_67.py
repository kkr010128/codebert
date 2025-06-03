n = int(input())
x = str(input())

one = x.count("1")
X = int(x, 2)

if one==1:
    for i in range(n):
        if x[i]=="1":
            print(0)
        elif i==n-1:
            print(2)
        else:
            print(1)
    
    
elif one>1:
    
    Xp = X % (one+1)
    Xm = X % (one-1)

    def f(x):
        if x==0:
            return 0
        return 1+f(x%bin(x).count("1"))

    for i in range(n):
        
        if x[i]=="0":
            c = pow(2, n-i-1, one+1)
            print(f((Xp+c)%(one+1))+1)
        else:
            c = pow(2, n-i-1, one-1)
            print(f((Xm-c)%(one-1))+1)
else:
    for i in range(n):
        print(1)