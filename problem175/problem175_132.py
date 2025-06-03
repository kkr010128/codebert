N = int(input())
S = str(input())

r_cnt = S.count('R')
g_cnt = S.count('G')
b_cnt = S.count('B')

ans = r_cnt*g_cnt*b_cnt

for i in range(N):
    for d in range(1, N):
        j = i + d
        k = j + d
        if k >= N:break
        if S[i]!=S[j] and S[i]!=S[k] and S[j]!=S[k]:
            ans -= 1

print(ans)