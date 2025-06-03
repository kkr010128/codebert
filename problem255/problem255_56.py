N = int(input())
S, T = input().split()
A = ""
for i in range(N):
    A += S[i] + T[i]
print(A)