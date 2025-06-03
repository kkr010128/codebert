n = int(input())
S = [c for c in input()]
ans = 0
i = 0
j = n-1
while i < j:
    if S[i] == "W":
        if S[j] == "R":
            S[i] = "R"
            S[j] = "W"
            j -= 1
            i += 1
            ans += 1
        else:
            j -= 1
    else:
        i += 1
print(ans)