S = input()
ans = {0:1}
memo = [0]
last = 1
for ind, s in enumerate(S[::-1]):
    memo.append((int(s) * last + memo[-1]) % 2019)
    last *= 10
    last %= 2019
    if(memo[-1] in ans):
        ans[memo[-1]] += 1
    else:
        ans[memo[-1]] = 1

res = 0
for key in ans.keys():
    res += ans[key]*(ans[key]-1)//2
print(res)