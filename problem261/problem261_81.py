S = input()
S_rev = S[::-1]

cnt = 0
for i in range(len(S) // 2):
    if S[i] != S_rev[i]:
        cnt = cnt + 1
print(cnt)
