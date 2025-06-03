N = int(input())
S, T = list(map(str, input().split()))

A = ''
for i in range(N):
    A += S[i]
    A += T[i]

print(A)