N = int(input())
A = list(map(int,input().split()))
tot = sum(A)
D = {}
for i in range(N):
    a = A[i]
    if a not in D:
        D[a] = 0
    D[a] += 1
Q = int(input())
for _ in range(Q):
    b,c = map(int,input().split())
    if b not in D:
        print(tot)
    else:
        d = c-b
        if c in D:
            n = D[b]
            D[c] += D[b]
            del D[b]
        else:
            n = D[b]
            D[c] = D[b]
            del D[b]
        tot += n*d
        print(tot)