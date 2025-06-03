S=int(input())
dp=[]#答えの方
assim=[]#累積和
mod=10**9+7

for i in range(2001):
    if i<3:
        dp.append(0)
    elif i==3:
        dp.append(1)
    else:
        dp.append((assim[-3])%mod)
    
    if i==0:
        assim.append(0)
    else:
        assim.append((assim[-1]+dp[-1])%mod)

print(assim[S])