s = input()
n = len(s)
dp = [0 for _ in range(n)]
dp[-1] = int(s[-1])
memo = 0
cnt_dic = {}
tmp = 1
ans = 0
cnt_dic[0] = 1
for i in range(n-1, -1, -1):
    memo = (memo + int(s[i]) * pow(10, n-i-1, 2019)) % 2019
    if not memo in cnt_dic:
        cnt_dic[memo] = 0
    ans += cnt_dic[memo]
    cnt_dic[memo] += 1

print(ans)