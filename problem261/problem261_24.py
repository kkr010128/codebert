S = input()
N = len(S)
ans = 0
for k in range(N//2):
    if S[k] != S[-k-1]:
        ans += 1
print(ans)
