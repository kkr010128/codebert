mod=10**9+7
def fact(n):
    ans=1
    for i in range(1,n+1):
        ans*=i
        ans%=mod
    return ans

x,y=map(int,input().split())
if (x+y)%3!=0: print(0)
else:
    temp=(x+y)//3
    if x<temp or x>2*temp: print(0)
    else:
        dx=x-temp
        fc_temp=fact(temp)
        fc_dx=fact(dx)
        fc_temp_dx=fact(temp-dx)
        fc_dx=pow(fc_dx,mod-2,mod)
        fc_temp_dx=pow(fc_temp_dx,mod-2,mod)
        ans=fc_temp*fc_dx%mod*fc_temp_dx%mod
        print(ans)