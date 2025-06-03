S = input()
T = input()
N = len(S)
cnt = 0
for i in range(N):
    if S[i] != T[i]:
        cnt += 1
    else:
        cnt += 0

print(cnt)