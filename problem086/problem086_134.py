N,X,T = map(int,input().split())
num = N//X
mode = N%X
if mode == 0:
    print(num * T)
else:
    print((num + 1)*T) 