S = input()
L = len(S)
cnt = 0
for i in range(L//2):
    if S[i] == S[-1-i]:
        continue
    else:
        cnt += 1
print(cnt)