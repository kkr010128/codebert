N,X,T = map(int,input().split())

quo,mod  = divmod(N,X)

if mod == 0:
    print(T*quo)
else:
    print(T*(quo+1))