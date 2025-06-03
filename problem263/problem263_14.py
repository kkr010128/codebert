from copy import copy
n = int(input())
a_ls = list(map(int, input().split()))
c_bin = [[0]*60 for _ in range(n)]
a_bin_ls = [[0]*60 for _ in range(n)]
now_bin = [0] * 60
for i in range(n-1,-1,-1):
    a = a_ls[i]
    j = 0
    while True:
        if a == 1:
            now_bin[j] += 1
            a_bin_ls[i][j] = 1
            break
        elif a == 0:
            break
        a,r = divmod(a,2)
        now_bin[j] += r 
        a_bin_ls[i][j] = r
        j += 1
    c_bin[i] = copy(now_bin)
ans_bin = [0]*60
for i in range(n-1):
    a_bin = a_bin_ls[i]
    for j in range(60):
        if a_bin[j] == 0:
            times = c_bin[i+1][j]
        else:
            times = n - (i+1) - c_bin[i+1][j]
        ans_bin[j] += times
ans = 0
mod = 10**9+7
for i in range(60):
    ans += 2**i * (ans_bin[i]%mod)
    ans %= mod
print(ans)


