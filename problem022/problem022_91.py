nS = int(input())
S = list(map(int,input().split()))
nQ = int(input())
Q = list(map(int,input().split()))

cnt = 0

for i in range(nQ):
    copy_S = S.copy()
    copy_S.append(Q[i])

    j = 0
    while copy_S[j] != Q[i]:
        j += 1
    if j < len(copy_S)-1 : cnt += 1

print(cnt)
