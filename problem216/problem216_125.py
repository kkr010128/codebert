A = input().split()

a = A.count(A[0])
b = A.count(A[1])
c = A.count(A[2])

if a == 2 or b == 2 or c == 2:
    print("Yes")
else:
    print("No")
