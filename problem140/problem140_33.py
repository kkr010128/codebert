S = input()
ans=""

for i in range(len(S)):
    if S[i] == "?":
        ans += "D"
    else:
        ans += S[i]

print(ans)