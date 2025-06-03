N,A,B = map(int, input().split())

C = A + B

print(min(A, N%C) + N//C * A)