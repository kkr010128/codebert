S = list(input())
N = len(S)

if N % 2 == 0:
    m = int(N/2)
    LS = S[:m]
    RS = S[N:m-1:-1]
    ans = 0
    for i in range(m):
        if LS[i] == RS[i]:
            pass
        else:
            ans += 1
else:
    m = int((N+1)/2)
    LS = S[:m-1]
    RS = S[N:m-1:-1]
    ans = 0
    for i in range(m-1):
        if LS[i] == RS[i]:
            pass
        else:
            ans += 1

print(ans)