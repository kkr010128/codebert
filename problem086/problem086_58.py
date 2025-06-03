N,X,T = map(int,input().split())
res = N*T//X
div = res//T
mod = res%T
if mod == 0:
    print (res)
else :
    print ((div+1)*T)
