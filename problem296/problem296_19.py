S = input()
K = int(input())
S2 = S + S
ans = 0
s = S[0]
if len(set(S)) == 1:
    print(len(S) * K // 2)
else:
    for i in range(1, len(S2)):
        if s == S2[i]:
            ans += 1
            s = '1'
        else:
            s = S2[i]

    if ans % 2 == 0:
        ans = ans // 2 * K
    else:
        ans = (ans + 1) // 2 * K - 1

    print(ans)