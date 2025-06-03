S = input()
T = input()

s = len(S)
t = len(T)

ans = t
for j in range(s - t + 1):
    val = 0
    for i in range(t):
        if S[j:j + t][i] != T[i]:
            val += 1
    ans = min(ans, val)
print(ans)
