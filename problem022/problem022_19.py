n = input()

S = map(int, raw_input().split())

q = input()

T = map(int, raw_input().split())

S.append(0)
cnt = 0
for i in range(q):
    j = 0
    S[n] = T[i]
    while S[j] != S[n]:
        j = j + 1
    if j != n:
        cnt = cnt + 1


print cnt