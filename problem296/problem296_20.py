S = input()
K = int(input())

if S.count(S[0]) == len(S):
    print(len(S)*K//2)
    exit()

count = 0
i = 1
flg = [False] * len(S)
while i < len(S):
    if S[i] == S[i-1]:
        count += 1
        flg[i] = True
        i += 2
    else:
        i += 1
count *= K
if (not flg[len(S)-1]) and S[0] == S[-1]:
    a = 1
    for i in range(1, len(S)):
        if S[0] == S[i]:
            a += 1
        else:
            break
    if a % 2 == 1:
        count += (K-1)
print(count)
