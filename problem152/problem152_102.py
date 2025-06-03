n = int(input())
s = [""]*n
dp = [[] for i in range(n+1)]
plus = []
minas = []
pgomi = []
mgomi = []
kosu = 0
for i in range(n):
    s[i] = input()
    dp[i] = [0]*(len(s[i]) + 1)
    check = True
    kosu += len(s[i])
    moi = 0
    for j in range(len(s[i])):
        p = 0
        if s[i][j] == '(':p = 1
        else:p = -1
        moi += p
        dp[i][j+1] = dp[i][j] + p
    saisyo = min(dp[i])
    if saisyo >= 0:plus.append(i)
    elif saisyo == dp[i][-1]:minas.append(i)
    elif dp[i][-1] >= 0:pgomi.append([moi,i])
    else:mgomi.append([moi,i])
pgomi.sort(reverse = True)
mgomi.sort(reverse = True)
ruiseki = [0]*(10**6+5)
idx = 0
for i in plus + [v[1] for v in pgomi] + [v[1] for v in mgomi] + minas:
    for j in range(len(s[i])):
        p = 0
        if s[i][j] == '(':p = 1
        else:p = -1
        ruiseki[idx+1] = ruiseki[idx] + p
        idx += 1
check = True
for i in range(kosu):
    if ruiseki[i+1] < 0:
        check = False
        break
if check == False or ruiseki[kosu] != 0:
    print("No")
else:
    print("Yes")