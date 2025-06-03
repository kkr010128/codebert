N,K,S = [int(hoge) for hoge in input().split()]
import math
#累積和数列であって、Ar-Al=Sを満たすものが丁度K個ある
if S==10**9:
    print(*([S]*K + [27]*(N-K)))

elif S:
    print(*([S]*K + [S+1]*(N-K)))
else:
    ans = []
    while 1:
        if K==2:
            ans +=[0,1,0]
            break            
        for R in range(N):
            if (R+1)*(R+2)//2 > K:break
        print(K)
        if K==0:break
        ans += [0]*R+[1]
        K = K - R*(R+1)//2 
        
    print(ans + [1]*(N-len(ans)))