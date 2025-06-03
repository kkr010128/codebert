S = input()
T = input()
Ns = len(S)
Nt = len(T)

ans = 0
for i in range(Ns - Nt + 1):
    tmp = 0
    for j in range(Nt):
        if S[i + j] == T[j]:
            tmp += 1
        ans = max(ans, tmp)
print(Nt - ans)