S = input()
T = input()
ans = 1e10
for i in range(len(S)):
    if i+len(T) > len(S):
        break
    cnt = 0
    for j in range(len(T)):
        if S[i+j] != T[j]:
            cnt += 1
    ans = min(cnt, ans)
print(ans)
