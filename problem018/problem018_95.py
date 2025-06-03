L = input().split()
n = len(L)
A  = []
top = -1
for i in range(n):
    if L[i] not in {"+","-","*"}:
        A.append(int(L[i]))
        top += 1
    else:
        if(L[i] == "+"):
            A[top - 1] = A[top - 1] + A[top]
        elif(L[i] == "-"):
            A[top - 1] = A[top -1] - A[top]
        elif(L[i] == "*"):
            A[top - 1] = A[top - 1] * A[top]
        del A[top]
        top -= 1
print(A[top])
