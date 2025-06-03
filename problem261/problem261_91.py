S = input()
N = len(S)
if N % 2 == 0:
    tmp = N // 2
else:
    tmp = (N + 1) // 2
ans = 0
for i in range(tmp, N):
    if S[i] != S[N - i - 1]:
        ans += 1
print(ans)
