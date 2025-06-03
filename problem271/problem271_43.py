N = int(input())
S = input()

A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

T = str.maketrans(A, A[N:] + A[:N])

print(S.translate(T))