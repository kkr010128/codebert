A,B = input().split()
A = int(A)
x = ""
for i in range(len(B)):
    if B[i]!=".":
        x += B[i]
B = int(x)
C = A*B
C = C//100
print(C)