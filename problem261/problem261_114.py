S = input().strip()
N = len(S)
cnt = 0
for i in range(N//2):
    if S[i]!=S[N-1-i]:
        cnt += 1
print(cnt)