N = int(input())
A = list(map(int,input().split()))
ans = sum(A)

X = [0]*(10**5+1)

for x in A:
    X[x] += 1

Q = int(input())

for _ in range(Q):
    B,C = map(int,input().split())
    ans += (C-B)*X[B]
    X[C] += X[B]
    X[B] = 0
    print(ans)
