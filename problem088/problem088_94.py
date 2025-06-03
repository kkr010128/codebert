N = int(input())
A = list(map(int, input().split()))

M = 0
S = 0

for a in A:
    if M < a:
        M = a
    if a < M:
        S += M - a

print(S)