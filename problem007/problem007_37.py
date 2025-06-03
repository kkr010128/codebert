
fibo_list=[0 for i in range(48)]

def fibo(n):
    f=fibo_list[n]
    if f:
        return f
    else:
        if n==0 or n==1:
            return 1
        else:
            f=fibo(n-1)+(fibo(n-2))
    fibo_list[n]=f
    return f


n=input()
print(fibo(n))