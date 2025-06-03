A, B, C = input().split()

A = int(A)
B = int(B)
C = int(C)

A, B, C = B, A, C
B, A, C = C, A, B
C, A, B = A, B, C

print(A, B, C)
