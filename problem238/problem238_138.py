n,k,s = map(int,input().split())
if s != 10**9:
    ans_ls = [s+1] * n
    for i in range(k):
        ans_ls[i] = s
    ans_ls = list(map(str,ans_ls))
else:
    ans_ls = [1] * n
    for i in range(k):
        ans_ls[i] = s
    ans_ls = list(map(str,ans_ls))
print(' '.join(ans_ls))
