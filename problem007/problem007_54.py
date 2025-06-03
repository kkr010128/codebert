
n=int(input())
f=[0]*45
def Fib(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        if f[n]!=0:
            return f[n]
        else:
            f[n]=Fib(n-1)+Fib(n-2)
            return f[n]
print(Fib(n))
    
