# B - Substring

S = str(input())
T = str(input())

s = len(S)
t = len(T)
ans = 10**18

for i in range(s-t+1):
    tmp = 0
    for j in range(t):
        if S[i+j] == T[j]:
            continue
        else:
            tmp += 1
    ans = min(ans, tmp)

print(ans)