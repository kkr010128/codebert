s = "0" + input()
keta = len(s)
dp = [0] * (keta + 1)
kuri = 0
for i in range(keta):
    ni = i + 1
    num = int(s[-i - 1])
    if kuri:
        num += 1
        kuri = 0
    if num == 10:
        kuri = 1
        dp[ni] = dp[i]
    elif num < 5:
        dp[ni] = dp[i] + num
    elif num > 5:
        num %= 10
        kuri = 1
        dp[ni] = dp[i] + 10 - num
    else:
        nn = int(s[-ni - 1])
        if nn < 5:
            dp[ni] = dp[i] + num
        else:
            kuri = 1
            dp[ni] = dp[i] + 10 - num
print(dp[keta] + kuri)
