s = input()
l = len(s)
S = list(s)
ans = 0

for i in range(l//2):
    if S[i] != S[l-i-1]:
        S[i-1] = S[l-i-1]
        ans += 1

print(ans)