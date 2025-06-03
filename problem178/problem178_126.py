A, B, C = map(int, input().split())
temp = B
B = A
A = temp
temp = C
C = A
A = temp
print(str(A) + " " + str(B) + " " + str(C))