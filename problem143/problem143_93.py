K = int(input())
S = input()
ans = ""
if K >= len(S):
    print(S)
else:
    for i in range(K):
        ans += S[i]
    print(ans + "...")