# 集合A={2,3},B={2,4},C={3,5,7}がある。
# それぞれの集合から1つずつa,b,cを選ぶ。
# a+b+c = nとなる選び方は何通りあるか。
# ->    f = (x^2+x^3)*(x^2+x^4)*(x^3+x^5+x^7)とするとき、fのx^nの係数が答え
# -->   [x^n](x^2+x^3)(x^2+x^4)*(x^3+x^5+x^7)と表される。


# f = x^3 + x^4 + x^5 + ...
#[x^s]f^n
#->[x^s](for i in range(∞):f^n)

#A[n] = A[n-3] +A[n-4] +A[n-5] + ... + A[0]
#A[0] = 1

s = int(input())
MODINT = 1000000007
dp = [0]*(s+1)
dp[0] = 1

for i in range(1,s+1):
    for j in range(0,(i-3)+1):
        dp[i] += dp[j]
        dp[i] %= MODINT
print(dp[s])