#解説参照
#i桁目で10^i円多くはらうか否か

n_ =list(input())
n = [int(i) for i in n_]
ans = 0
if len(n_)==1:
    print(min(n[0],11-n[0]))
    exit()
dp1 = 0
dp2 = 1

for i in range(len(n)):
    dp_1 = min(dp1+n[i],dp2+10-n[i])
    dp_2 = min(dp1+n[i]+1,dp2+9-n[i])
    dp1 = dp_1
    dp2 = dp_2
print(dp1)
