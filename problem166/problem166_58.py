s = input()
n = len(s)
dp = [0 for _ in range(n)]
dp[-1] = int(s[-1])
cnt_dic = {}
tmp = 1
ans = 0
cnt_dic[0] = 1
cnt_dic[dp[-1]] = 1
for i in range(n-2, -1, -1):
    dp[i] = (dp[i+1] + int(s[i]) * pow(10, n-i-1, 2019)) % 2019
    if not dp[i] in cnt_dic:
        cnt_dic[dp[i]] = 0
    ans += cnt_dic[dp[i]]
    cnt_dic[dp[i]] += 1

print(ans)