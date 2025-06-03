N,X,T=map(int,input().split())
a=N//X
b=N%X
if b!=0:
    print((a+1)*T)
else:
    print(a*T)