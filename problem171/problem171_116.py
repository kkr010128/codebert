# ai の大きい方から左端か右端
# はるかに問題なのはそこから先だがDP
n=int(input())
*a,=map(int, input().split( ))
dp = [0]
#周回が総数、dpのindexが左に置いた数
aii = [(ai,i) for i,ai in enumerate(a)]
aii.sort(key= lambda x:-x[0])
for j,(ai,i) in enumerate(aii):
    dp2 = [0]*(j+2)
    dp2[0]=dp[0]+ai*abs(n-j-1-i)
    dp2[-1]=dp[-1]+ai*abs(j-i)
    for k in range(j):
        dp2[k+1] = max(dp[k]+ai*abs(k-i), dp[k+1]+ai*abs((n-(j-k-1)-1)-i))##abs((n-(j-k-1)-1)-i)
    dp = dp2

print(max(dp))