N = int(input())
A = [int(i) for i in input().split()]
B = set(A)
b = len(B)

if N == b:
    print('YES')
else:
    print('NO')