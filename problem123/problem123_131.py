N = int(input())

P = 0

A = list(map(int,input().split()))

for i in range(N):
    P = P ^ A[i]

ans = [A[i] ^ P for i in range(N)]

print(" ".join(map(str,ans)))