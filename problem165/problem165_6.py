N = int(input())
S = [input() for i in range(N)]
S.sort()
cnt = 1
for i in range(1, N):
    if S[i]!=S[i-1]:
        cnt += 1
print(cnt)