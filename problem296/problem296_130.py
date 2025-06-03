S = input()
K = int(input())

N = len(S)
p = S[0]
c = 0

if N == 1:
    print(K//2)
    exit()

if len(set(S)) == 1:
    print(N*K//2)
    exit()

for i in range(1,N):
    if S[i] == p:
        c += 1
        p = ''
    else:
        p = S[i]

ans = c*K
if S[0] == S[-1]:
    p = S[0]
    c = 1
    for i in range(1,N):
        if p == S[i]:
            c += 1
        else:
            break

    d = 1
    for i in range(2,N+1):
        if p == S[-i]:
            d += 1
        else:
            break

    if (c%2)*(d%2) == 1:
        ans += K-1

print(ans)
