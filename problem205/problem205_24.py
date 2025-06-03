N, P = map(int, input().split())
S = input()

a = [0] * (N + 1)

if P != 2 and P != 5:
    tenfactor=1
    for i in range(1,N+1):
        a[i] = ((int(S[N-i])*tenfactor+a[i-1])%P)
        tenfactor*=10
        tenfactor%=P

    ans = 0
    from collections import Counter
    C=Counter(a)
    for v,i in C.items():
        ans += (i * (i - 1) // 2)
elif P == 2:
    ans = 0
    for i in range(N):
        if int(S[i]) % 2 == 0:
            ans += i + 1
elif P == 5:
    ans = 0
    for i in range(N):
        if int(S[i]) == 0 or int(S[i]) == 5:
            ans += i + 1

print(ans)

