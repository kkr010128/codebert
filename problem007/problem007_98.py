a=[0]*45

def Fib(n):
    if n == 0:
        a[0]=1
        return 1
    elif n == 1:
        a[1]=1
        return 1
    else:
        if a[n]==0:
            a[n]=Fib(n-1)+Fib(n-2)
            return a[n]
        else:
            return a[n]
    
n=int(input())
print(Fib(n))


