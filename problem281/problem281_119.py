X,Y=map(int,input().split())
mod=10**9+7
if (X+Y)%3!=0:
    print(0);exit()
if X*2<Y or Y*2<X:
    print(0);exit()
t=(X+Y)//3
f=[1]
for i in range(1,t+100):
    f.append(f[-1]*i%mod)
def comb(a,b,m):
    return f[a]*pow(f[b],m-2,m)*pow(f[a-b],m-2,m)%m
print(comb(t,X-t,mod))
